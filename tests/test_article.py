import unittest
from unittest.mock import patch, mock_open, MagicMock, call
import os
import csv
from data_class.article import Article 

class TestArticle(unittest.TestCase):
    
    @patch("os.path.exists")
    @patch("os.makedirs")
    @patch("shutil.copy")
    def test_display_pdf_article_file_exists(self, mock_copy, mock_makedirs, mock_exists):
        """Test the display_pdf_article method when the file exists."""
        mock_exists.return_value = True
        article = Article("sample.pdf")
        
        with patch("builtins.print") as mock_print:
            article.display_pdf_article()
            download_path = os.path.join("./downloads", "sample.pdf")
            mock_copy.assert_called_once_with("sample.pdf", download_path)
            mock_print.assert_called_once_with(f"The file has been 'downloaded' to {download_path}")

    @patch("os.path.exists")
    @patch("os.makedirs")
    @patch("shutil.copy", side_effect=FileNotFoundError)
    def test_display_pdf_article_file_not_found(self, mock_copy, mock_makedirs, mock_exists):
        """Test the display_pdf_article method when the file is not found."""
        mock_exists.return_value = False
        article = Article("missing.pdf")
        
        with patch("builtins.print") as mock_print:
            article.display_pdf_article()
            mock_makedirs.assert_called_once_with("./downloads")
            mock_print.assert_called_once_with("File not found: missing.pdf")

    @patch("builtins.open", new_callable=mock_open, read_data="title,description\nTitle1,Description1\nTitle2,Description2\n")
    def test_display_csv_article(self, mock_file):
        """Test the display_csv_article method for a valid CSV file."""
        article = Article("sample.csv")
        
        with patch("builtins.print") as mock_print:
            article.display_csv_article()
            expected_calls = [
                call("Title1: Description1\n"),
                call("\n" + "-" * 70 + "\n"),
                call("Title2: Description2\n"),
                call("\n" + "-" * 70 + "\n")
            ]
            mock_print.assert_has_calls(expected_calls, any_order=False)
            mock_file.assert_called_once_with("sample.csv")

    @patch("builtins.open", new_callable=mock_open)
    def test_display_csv_article_file_not_found(self, mock_file):
        """Test the display_csv_article method when the file is not found."""
        mock_file.side_effect = FileNotFoundError
        article = Article("missing.csv")
        
        with patch("builtins.print") as mock_print:
            article.display_csv_article()
            mock_print.assert_called_once_with("File not found: missing.csv")

    @patch("builtins.open", new_callable=mock_open, read_data="invalid,csv,data")
    def test_display_csv_article_csv_error(self, mock_file):
        """Test the display_csv_article method when there is a CSV error."""
        article = Article("corrupt.csv")
        
        with patch("csv.DictReader", side_effect=csv.Error), patch("builtins.print") as mock_print:
            article.display_csv_article()
            mock_print.assert_called_once_with("csv file error: ")

if __name__ == "__main__":
    unittest.main()
