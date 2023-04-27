#!/bin/bash

cd /tmp
rm -rf /tmp/sd-ansible-colab
git clone https://github.com/epava1516/sd-ansible-colab.git
cd /tmp/sd-ansible-colab
rm -rf .git/
ansible-playbook main.yml
cd /content
