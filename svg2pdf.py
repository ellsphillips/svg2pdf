from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os


class SVGtoPDF:
    def __init__(self, directory):
        self.directory = directory
        self._in = "svg/"
        self._out = "pdf/"
        self.from_extension = '.svg'
        self.to_extension = '.pdf'

    def get_svg_list(self):
        """
        Retrieve all SVG files in root directory and below.

        parameters: none
        returns: List of SVG file paths
        """
        svg_list = []
        for path, subdirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith(self.from_extension):
                    abspath_file = path + os.sep + file
                    svg_list.append(abspath_file)
        print('{} SVG files found in directory'.format(len(svg_list)))
        return svg_list

    def svg_pdf(self, svg_list):
        """
        Convert all svg files to pdf

        parameters:
            svg_list: list of SVG filepaths to convert and export

        returns: none
        """
        print('\nConverting, please wait...\n')
        for svg in svg_list:
            pdf_abspath = svg.split('\\')[-1]
            pdf_name = pdf_abspath.split('.')[0]
            print('Converting file: {}'.format(pdf_abspath))
            drawing = svg2rlg(self._in + pdf_abspath)
            renderPDF.drawToFile(drawing, self._out + pdf_name + self.to_extension)

    def clean_outputs(self, pdf_list):
        print("Refactoring files...")
        for pdf in pdf_list:
            os.rename(
                self.directory + self._out + pdf,
                self.directory + self._out + pdf.split("_")[-1]
            )


def main():
    formatter = SVGtoPDF(os.getcwd())
    svg_files = formatter.get_svg_list()
    formatter.svg_pdf(svg_files)

    pdf_list = [_file for _file in os.listdir("pdf/") if os.path.isfile(os.path.join("pdf/", _file))]

    print(pdf_list)

    formatter.clean_outputs(pdf_list)


if __name__ == "__main__":
    main()
