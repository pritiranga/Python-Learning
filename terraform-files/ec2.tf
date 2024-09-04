# creating key-pair
resource "aws_key_pair" "my_key_pair" {
  key_name = "devops-terra"
  public_key = file("~/.ssh/devops-terra.pub")
}

output "private_key" {
  value = aws_key_pair.my_key_pair.key_name
  sensitive = true
}

# creating vpc
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "terra-VPC"
  }
}

# creating internet gateways
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "terra-InternetGateway"
  }
}

# creating subnet
resource "aws_subnet" "my_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "eu-north-1a" 
  tags = {
    Name = "terra-Subnet"
  }
}

# Creating route table
resource "aws_route_table" "my_route_table" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_igw.id
  }

  tags = {
    Name = "terra-RouteTable"
  }
}

# Associating route table with subnet
resource "aws_route_table_association" "my_route_table_ass" {
  subnet_id      = aws_subnet.my_subnet.id
  route_table_id = aws_route_table.my_route_table.id
}

#Creating security groups
resource "aws_security_group" "my_sg" {
  vpc_id = aws_vpc.my_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"    # -1 means all protocols
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "terra-SecurityGroup"
  }
}

# Creating ec2
resource "aws_instance" "my_ec2_instance" {
  ami           = var.ami_id  
  instance_type = var.instance_type
  
  subnet_id              = aws_subnet.my_subnet.id
  vpc_security_group_ids = [aws_security_group.my_sg.id]

  key_name = "devops-terra"  

  tags = {
    Name = "terra-EC2Instance"
  }
}
