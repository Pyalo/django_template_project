from encodings import iso2022_kr

from django.test import TestCase


class PageViewTests(TestCase):
    def test_page_routes_render(self):
        routes = (
            "",
            "about/",
            "services/",
            "team/",
            "portfolio/",
            "portfolio/details/",
            "blog/",
            "blog/details/",
            "contact/",
        )
        for route in routes:
            with self.subTest(route=route):
                response = self.client.get("/" + route)
                self.assertEqual(response.status_code, 200)
