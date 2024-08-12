import os
import shutil
import csv


class Article:
    """Displays articles for child classes"""

    def __init__(self, filename):
        self.filename = filename
        self.text_data = ""

    def display_pdf_article(self):
        """Display's pdf articles (.pdf) files"""

        download_path = "./downloads"

        try:
            if not os.path.exists(download_path):
                os.makedirs(download_path)

            download_file_path = os.path.join(
                download_path, os.path.basename(self.filename)
            )

            shutil.copy(self.filename, download_file_path)
            print(f"The file has been 'downloaded' to {download_file_path}")
        except FileNotFoundError as e:
            print(f"File not found: {self.filename}")
        except Exception as e:
            print("Something unexpected occured: {e}")

    def display_csv_article(self):
        """Displays file extensions: .csv"""

        try:
            csv_data = []

            with open(self.filename) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    csv_data.append(
                        {"title": row["title"], "description": row["description"]}
                    )

                for row in csv_data:
                    print(f"{row['title']}: {row['description']}\n")
                    print("\n" + "-" * 70 + "\n")
        except FileNotFoundError as e:
            print(f"File not found: {self.filename}")
        except csv.Error as e:
            print(f"csv file error: {e}")
        except Exception as e:
            print("Something unexpected occured: {e}")
