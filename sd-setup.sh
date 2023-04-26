#!/bin/bash

%cd /tmp
!git clone https://github.com/epava1516/sd-ansible-colab.git
%cd /tmp/sd-ansible-colab
!ansible-playbook main.yml
%cd /content
