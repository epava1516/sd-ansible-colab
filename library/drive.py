from google.colab import drive
from ansible.module_utils.basic import AnsibleModule

def main():
    module_args = {
        'path': {
            'required': True,
            'type': 'str'
        },
    }

    result = {
        'changed': False,
        'message': ''
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    drive.mount(module.params['path'])
    result['message'] = "Mounted"
    result['changed'] = True

    module.exit_json(**result)

if __name__ == '__main__':
    main()
