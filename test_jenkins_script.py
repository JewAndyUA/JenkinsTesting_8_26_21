import argparse

class J:
    
    def __init__(self):
        """init"""
        self.arg_parser = argparse.ArgumentParser()
        
        self.arg_parser.add_argument(
            '--ip-address',
            help='The device IP address',
            required=True
        )
        self.arg_parser.add_argument(
            '--display-resolution',
            help='Optional. Device display resolution',
            type=str
        )
        self.arg_parser.add_argument(
            '--compare-language',
            help='Optional. ',
            type=str
        )
        self.arg_parser.add_argument(
            '--add-strings-mapping',
            help='Optional. ',
            action='store_true'
        )

        self.arg_parser.add_argument(
            '--full-table-of-content',
            help='Optional. Add expanded',
            action='store_true'
        )

        self.arg_parser.add_argument(
            '--verbose',
            help='Optional. Increase output verbosity',
            action='store_true'
        )
        
    def run(self):
        """Get args to call X execution method"""

        args = self.arg_parser.parse_args()

        parameters = {
            'ip_address': args.ip_address,
            'display_resolution': args.display_resolution,
            'compare_language': args.compare_language,
            'add_strings_mapping': args.add_strings_mapping,
            'full_table_of_content': args.full_table_of_content,
            'verbose': args.verbose
        }
        for key, value in parameters.items():
            print('%s: %s' % (key, value))
            
            
if __name__ == '__main__':
    J().run()
