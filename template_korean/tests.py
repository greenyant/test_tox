from django.test import TestCase

# Create your tests here.
class TempalteKoreanTestCase(TestCase):
	def setUp(self):
		pass
	def test_test(self):
		self.assertEqual(1,1)

	def test_korean_proofread_tag(self):
		from django.template import Context, Template
		rendered = Template('{% load proofread %}{{string|proofread}}').render(Context({
			'string': 'hi'
		}))
		self.assertEqual(rendered, 'hi')
