class Output_list:
    def __init__(self, io):
        self.io = io

    def output_list(self, output):
        for line in output:
            self.io.write(str(line)+'\n')
        return self.io

