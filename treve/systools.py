from subprocess import check_output
import logging

def get_sel():
    selected_str = check_output(['xsel','-o']).decode('utf-8')
    # import ipdb; ipdb.set_trace()
    logging.debug('Selected: {}'.format(selected_str))
    if not selected_str:
        logging.error('Nothing selected')
        return False
    return selected_str

def main():
    get_sel()

if __name__ == '__main__':
    main()
