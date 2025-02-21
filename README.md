# Terraform + Ansible EC2 Project

This project uses Terraform to provision load-balanced EC2 instances and Ansible to configure them.

## Prerequisites
- Terraform
- Ansible
- AWS CLI

## Usage
1. Run Terraform to provision infrastructure:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

2. Run Ansible to configure servers:
   ```bash
   cd ../ansible
   ansible-playbook -i inventory/hosts playbooks/configure_servers.yml
   ```

3. Use GitHub Actions to automate the deployment.
# terraform-ansible-cloud-automation
