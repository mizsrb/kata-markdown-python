import pytest as pytest
from assertpy import assert_that

from markdown_links_to_footnotes_use_case import MarkdownLinksToFootnotesUseCase


class TestMarkdownLinksToFootnotesUseCase:
    def test_should_write_file_with_transformed_markdown_in_given_input_file(
        self,
    ):
        MarkdownLinksToFootnotesUseCase().execute("source.md", "destination.md")
        assert_that(True).is_false()

    @pytest.mark.skip()
    def test_should_throw_an_error_if_input_file_doesnt_exist(self):
        pass

    @pytest.mark.skip()
    def test_should_throw_an_error_if_output_file_already_exists(self):
        pass
