import boto3, json, ast
from datetime import datetime, timezone, timedelta

ec2 = boto3.client("ec2")
asg = boto3.client("autoscaling")
sns = boto3.client("sns")

def get_new_ami_from_sns_ec2imagebuilder(event):
    response = event["Records"][0]["Sns"]["Message"]
    #print(response)
    #print(type(response))
    new_ami = ast.literal_eval(response)
    #print(new_ami)
    new_ami = new_ami['Records'][0]['Sns']['Message']
    #print(new_ami)
    #print(type(new_ami))
    new_ami = json.loads(new_ami)
    #print(new_ami)
    new_ami = new_ami['outputResources']['amis'][0]
    #print(new_ami)
    
    return new_ami
    
def update_current_launch_template_ami(launch_template_id, ami):
    response = ec2.create_launch_template_version(
        LaunchTemplateId=launch_template_id,
        SourceVersion="$Latest",
        VersionDescription="Latest-AMI",
        LaunchTemplateData={
            "ImageId": ami
        }
    )
    print(f"New launch template created with AMI {ami}")
    
def set_launch_template_default_version(launch_template_id):
    response = ec2.modify_launch_template(
        LaunchTemplateId=launch_template_id,
        DefaultVersion="$Latest"
    )
    print("Default launch template set to $Latest.")
    previous_version = str(
        int(response["LaunchTemplate"]["LatestVersionNumber"]) - 2)
    response = ec2.delete_launch_template_versions(
        LaunchTemplateId=launch_template_id,
        Versions=[
            previous_version,
        ]
    )
    print(f"Old launch template {previous_version} deleted.")

def create_asg_scheduled_action(asg_name, start_time, desired_capacity):
        response = asg.put_scheduled_update_group_action(
            AutoScalingGroupName=asg_name,
            ScheduledActionName=f"Desire {desired_capacity}",
            StartTime=start_time,
            DesiredCapacity=desired_capacity
        )
        print(f"""
            ASG action created
            Start time: {start_time}"
            Desired capacity: {desired_capacity}
            """)
            
def lambda_handler(event, context):
    # Get new ami from sns EC2 image builder
    new_ami = get_new_ami_from_sns_ec2imagebuilder(event)
    new_ami_id = new_ami['image']
    new_ami_name = new_ami['name']
    
    print("New AMI ID   = ", new_ami_id)
    print("New AMI Name = ", new_ami_name)
    
    # update new ami in launch template
    launch_template_id = "lt-04d87d108878b44e5"
    
    update_current_launch_template_ami(launch_template_id, new_ami_id)
    set_launch_template_default_version(launch_template_id)
    
    # Create future ASG actions to roll out the new AMI
    asg_name = "Test_ASG"
    now_utc = datetime.now(timezone.utc)
    in_01_min = now_utc + timedelta(minutes=1)
    in_15_min = now_utc + timedelta(minutes=15)
    
    create_asg_scheduled_action(asg_name, in_01_min, 2)
    create_asg_scheduled_action(asg_name, in_15_min, 1)
    
    return {
        'statusCode': 200
    }
