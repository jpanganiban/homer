from jinja2 import Environment, PackageLoader
import os


env = Environment(loader=PackageLoader('homer', 'templates'))


class Homer(object):

    directories = ['bin', 'include', 'lib', 'local']

    # Files to write from a template and their corresponding
    # directory.
    templates = [
        ('activate', 'bin'),
        ('deactivate', 'bin'),
    ]

    def __init__(self, destination):
        self.current_path = os.getcwd()
        self.destination = destination
        self.destination_path = os.path.join(self.current_path, destination)

    @property
    def context(self):
        """Context for the template files"""
        return {
            'environment': self.destination,
            'environment_path': self.destination_path
        }

    def write_to_env(self, filename, contents, env_dir):
        """Writes a file to one of the environment's directories"""

        env_dir_path = os.path.join(self.destination_path, env_dir)

        with open(os.path.join(env_dir_path, filename), 'w') as f:
            f.write(contents)

    def create_environment(self):
        """Creates the environment files and directories."""

        # Create environment directory
        os.mkdir(self.destination_path)

        # Create the directories
        for dirname in self.directories:
            os.mkdir(os.path.join(self.destination_path, dirname))

        # Create the files
        for (template, env_dir) in self.templates:
            contents = env.get_template(template).render(**self.context)
            self.write_to_env(template, contents, env_dir)

        print "Done!"
