import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class TailwindExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(TailwindTreeprocessor(md), 'tailwind', 20)

class TailwindTreeprocessor(Treeprocessor):

    classes = {
        'h1': ['text-3xl', 'font-bold', 'mt-4'],
        'h2': ['text-2xl', 'font-bold', 'mt-4'],
        'h3': ['text-2xl', 'font-bold', 'mt-4'],
        'p': ['leading-relaxed'],
        'ul': ['list-disc', 'list-inside', 'mt-4', 'leading-tight'],
        'li': ['ml-4'],
    }
    def run(self, root):
        for node in root.iter():
            tag_classes = self.classes.get(node.tag)
            if tag_classes:
                node.attrib['class'] = ' '.join(tag_classes)









with open("temp.md", "r") as f:
    markdownstring = f.read()

htmlstring = markdown.markdown(markdownstring, extensions=[TailwindExtension()])

with open("temp.html", "w") as f:
    f.write(htmlstring)






