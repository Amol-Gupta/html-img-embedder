from click.testing import CliRunner
from html_img_embedder import main

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(main, [ r"C:\Users\amolg\source\repos\phm953\html-img-embedder\mnt\Slides_01.html", r"C:\Users\amolg\source\repos\phm953\html-img-embedder\mnt\build\Slides_01.html" ])
  assert result.exit_code == 0
  