import argparse
import panflute

class MarkdownLoader():
    # this really is just a place to stuff markdown processing functions, honestly.
    # I'm considering this self-documenting.
    def fromFileToString(self, filepath):
        ret = ""
        
        with open(filepath, "r") as file:
            ret = file.read()
            
        return ret
        
    def fromStringToAST(self, sourceString):
        # don't be a brain donor
        # it's meant for markdown format strings
        ret = None
        
        ret = panflute.convert_text(
                                        sourceString,
                                        input_format="markdown",
                                        output_format="panflute",
                                        standalone=True
                                   )
    
        return ret
    
    def fromFileToAST(self, filepath):
        ret = None
       
        swp = self.fromFileToString(filepath)
        ret = self.fromStringToAST(swp)
        
        return ret
        
class MarkdownASTTransfomer():
    # it looks more complicated than it really is. Promise.
    def __init__(self):
        # where to store parsed symbols from the walker.
        self.parsed = ""
        
        # where to store the current patchouli style data.
        # We care when we push and pop, mostly.
        self.style = []
    
    def perform(self, ast):
        ast.walk(self.transform)
        return self.parsed
    
    def addText(self, text):
        self.parsed = self.parsed + text
    
    def addStyles(self):
        for text in self.style:
            self.addText(text)
    
    def notImplementedErrorHelper(self, fragment, blockName):
        # helps build and throw not implemented errors.
        
        # print what we have anyway. Help me with stepwise doing this.
        print(self.parsed)
        
        errorStr =  (
                        f"Not implemented!\n"
                        f"\n"
                        f"Please submit your source file to greysondn's\n"
                        f"issue tracker!\n"
                        f"\n"
                        f"Type:\n"
                        f"{blockName} : {type(fragment)}\n"
                        f"\n"
                        f"Fragment:\n"
                        f"{panflute.stringify(fragment)}\n"
                        f"\n"
                    )
        
        raise NotImplementedError(errorStr)
    
    def transform(self, fragment, document=None):
        # eventually, this would transform the AST into patchouli's format.
        if type(fragment)   is panflute.BlockQuote:
            self.notImplementedErrorHelper(fragment, "BlockQuote")
        elif type(fragment) is panflute.BulletList:
            self.notImplementedErrorHelper(fragment, "BulletList")
        elif type(fragment) is panflute.Citation:
            self.notImplementedErrorHelper(fragment, "Citation")
        elif type(fragment) is panflute.Cite:
            self.notImplementedErrorHelper(fragment, "Cite")
        elif type(fragment) is panflute.Code:
            self.notImplementedErrorHelper(fragment, "Code")
        elif type(fragment) is panflute.CodeBlock:
            self.notImplementedErrorHelper(fragment, "CodeBlock")
        elif type(fragment) is panflute.Definition:
            self.notImplementedErrorHelper(fragment, "Definition")
        elif type(fragment) is panflute.DefinitionItem:
            self.notImplementedErrorHelper(fragment, "DefinitionItem")
        elif type(fragment) is panflute.DefinitionList:
            self.notImplementedErrorHelper(fragment, "DefinitionList")
        elif type(fragment) is panflute.Div:
            self.notImplementedErrorHelper(fragment, "Div")
        elif type(fragment) is panflute.Doc:
            # for now, just a metatag so I know what's going on.
            self.tfDoc(fragment, document)
        elif type(fragment) is panflute.Emph:
            # handled elsewhere
            pass
        elif type(fragment) is panflute.Header:
            self.notImplementedErrorHelper(fragment, "Header")
        elif type(fragment) is panflute.HorizontalRule:
            self.notImplementedErrorHelper(fragment, "HorizontalRule")
        elif type(fragment) is panflute.Image:
            self.notImplementedErrorHelper(fragment, "Image")
        elif type(fragment) is panflute.LineBlock:
            self.notImplementedErrorHelper(fragment, "LineBlock")
        elif type(fragment) is panflute.LineBreak:
            # handled elsewhere
            pass
        elif type(fragment) is panflute.LineItem:
            self.notImplementedErrorHelper(fragment, "LineItem")
        elif type(fragment) is panflute.Link:
            # links are also elsewhere
            pass
        elif type(fragment) is panflute.ListItem:
            self.notImplementedErrorHelper(fragment, "ListItem")
        elif type(fragment) is panflute.Math:
            self.notImplementedErrorHelper(fragment, "Math")
        elif type(fragment) is panflute.MetaBlocks:
            self.notImplementedErrorHelper(fragment, "MetaBlocks")
        elif type(fragment) is panflute.MetaBool:
            self.notImplementedErrorHelper(fragment, "MetaBool")
        elif type(fragment) is panflute.MetaInlines:
            self.notImplementedErrorHelper(fragment, "MetaInlines")
        elif type(fragment) is panflute.MetaList:
            self.notImplementedErrorHelper(fragment, "MetaList")
        elif type(fragment) is panflute.MetaMap:
            # it's apparently empty? I'mma print the darn thing
            # with an assert.
            testable = panflute.stringify(fragment)
            if (testable != ""):
                self.notimplementedErrorHelper(fragment, "MetaMap")
        elif type(fragment) is panflute.MetaString:
            self.notImplementedErrorHelper(fragment, "MetaString")
        elif type(fragment) is panflute.Note:
            self.notImplementedErrorHelper(fragment, "Note")
        elif type(fragment) is panflute.Null:
            self.notImplementedErrorHelper(fragment, "Null")
        elif type(fragment) is panflute.OrderedList:
            self.notImplementedErrorHelper(fragment, "OrderedList")
        elif type(fragment) is panflute.Para:
            self.tfParagraph(fragment, document)
        elif type(fragment) is panflute.Plain:
            self.notImplementedErrorHelper(fragment, "Plain")
        elif type(fragment) is panflute.Quoted:
            self.notImplementedErrorHelper(fragment, "Quoted")
        elif type(fragment) is panflute.RawBlock:
            self.notImplementedErrorHelper(fragment, "RawBlock")
        elif type(fragment) is panflute.RawInline:
            # I seem to have a long list of things handled elsewhere, non?
            pass
        elif type(fragment) is panflute.SmallCaps:
            self.notImplementedErrorHelper(fragment, "SmallCaps")
        elif type(fragment) is panflute.SoftBreak:
            self.notImplementedErrorHelper(fragment, "SoftBreak")
        elif type(fragment) is panflute.Space:
            # handled elsewhere
            pass
        elif type(fragment) is panflute.Span:
            self.notImplementedErrorHelper(fragment, "Span")
        elif type(fragment) is panflute.Str:
            # also handled elsewhere
            pass
        elif type(fragment) is panflute.Strikeout:
            # also handled elsewhere
            pass
        elif type(fragment) is panflute.Strong:
            # also handled elsewhere
            pass
        elif type(fragment) is panflute.Subscript:
            self.notImplementedErrorHelper(fragment, "SubScript")
        elif type(fragment) is panflute.Superscript:
            self.notImplementedErrorHelper(fragment, "Superscript")
        elif type(fragment) is panflute.Table:
            self.notImplementedErrorHelper(fragment, "Table")
        elif type(fragment) is panflute.TableCell:
            self.notImplementedErrorHelper(fragment, "TableCell")
        elif type(fragment) is panflute.TableRow:
            self.notImplementedErrorHelper(fragment, "TableRow")
        else:
            self.notImplementedErrorHelper(fragment, "UNRECOGNIZED")
            
            
    def tfDoc(self, fragment, document=None):
        # internals
        for child in fragment.content:
            if type(child) == panflute.Para:
                self.tfParagraph(fragment, document)
            else:
                self.notImplementedErrorHelper(child, "tfParagraph()")
    
    def tfEmph(self, fragment, document=None):
        # start italics
        self.addText("$(o)")
        
        # and append to formats currently active
        self.style.append("$(o)")
        
        # internals
        for child in fragment.content:
            if type(child) is panflute.Str:
                self.tfString(child, document)
            elif (type(child) == panflute.Strong):
                self.tfStrong(child, document)
            elif (type(child) == panflute.Space):
                self.tfSpace(child, document)
            elif (type(child) == panflute.Strikeout):
                self.tfStrikeOut(child, document)
            else:
                self.notImplementedErrorHelper(child, "tfEmph()")
                
        # close style and remove from active styles
        self.addText("$()")
        self.style.pop()
        
        # add remaining styles
        self.addStyles()
    
    def tfMetaMap(self, fragment, document=None):
        pass
        
    def tfParagraph(self, fragment, document=None):
    # I need to know if anything changes from start to end of this.
        lenAtStart = len(self.parsed)
    
        # internals
        for child in fragment.content:
            if   (type(child) == panflute.Str):
                self.tfString(child, document)
            elif (type(child) == panflute.Emph):
                self.tfEmph(child, document)
            elif (type(child) == panflute.Link):
                self.tfLink(child, document)
            elif (type(child) == panflute.Para):
                # what?
                pass
            elif (type(child) is panflute.RawInline):
                self.tfRawInline(child, document)
            elif (type(child) == panflute.Space):
                self.tfSpace(child, document)
            elif (type(child) == panflute.Strong):
                self.tfStrong(child, document)
            elif (type(child) == panflute.Strikeout):
                self.tfStrikeOut(child, document)
            elif (type(child) == panflute.LineBreak):
                self.tfLineBreak(child, document)
            else:
                self.notImplementedErrorHelper(child, "tfParagraph()")
        
        # only if we changed anything do we add more here)
        if (len(self.parsed) != lenAtStart):
            self.addText("$(br2)")
            self.addText("\n")
            self.addText("\n")
    
    def tfRawInline(self, fragment, document=None):
        if (fragment.format == "html"):
            if (fragment.text == "<kbd>"):
                self.addText("$(k:")
            elif (fragment.text == "</kbd>"):
                self.addText(")")
            else:
                self.notImplementedErrorHelper(fragment, "tfRawInline:html")
        else:
            self.notImplementedErrorHelper(fragment, "tfRawInline")
    
    def tfLineBreak(self, fragment, document=None):
        self.addText("$(br)")
        self.addText("\n")
        
    def tfLink(self, fragment, document=None):
        # url itself
        self.addText("$(l:")
        self.addText(fragment.url)
        self.addText(")")

        # believe it or not, they're also containers.
        for child in fragment.content:
            if   (type(child) == panflute.Str):
                self.tfString(child, document)
            else:
                self.notImplementedErrorHelper(child, "tfLink()")

        # and we need to close that link.
        self.addText("$(/l)")
    
    def tfSpace(self, fragment, document=None):
        self.addText(" ")
    
    def tfString(self, fragment, document=None):
        self.addText(fragment.text)
        
    def tfStrong(self, fragment, document=None):
        # start bold
        self.addText("$(l)")
        
        # and append to formats currently active
        self.style.append("$(l)")
        
        # internals
        for child in fragment.content:
            if type(child) is panflute.Str:
                self.tfString(child, document)
            elif (type(child) == panflute.Emph):
                self.tfEmph(child, document)
            elif (type(child) == panflute.Space):
                self.tfSpace(child, document)
            elif (type(child) == panflute.Strikeout):
                self.tfStrikeOut(child, document)
            else:
                self.notImplementedErrorHelper(child, "tfStrong()")
                
        # close style and remove from active styles
        self.addText("$()")
        self.style.pop()
        
        # add remaining styles
        self.addStyles()
        
    def tfStrikeOut(self, fragment, document=None):
        # start strikeout
        self.addText("$(m)")
        
        # and append to formats currently active
        self.style.append("$(m)")
        
        # internals
        for child in fragment.content:
            if type(child) is panflute.Str:
                self.tfString(child, document)
            elif (type(child) == panflute.Emph):
                self.tfEmph(child, document)
            elif (type(child) == panflute.Strong):
                self.tfStrong(child, document)
            elif (type(child) == panflute.Space):
                self.tfSpace(child, document)
            else:
                self.notImplementedErrorHelper(child, "tfStrikeout()")
                
        # close style and remove from active styles
        self.addText("$()")
        self.style.pop()
        
        # add remaining styles
        self.addStyles()
        
def main():
    # parse inputs
    parser  =   argparse.ArgumentParser(
                    description="Toolkit to convert markdown and yaml files " +
                                    "to patchouli's format",
                    usage="%(prog)s <command [options...]> <-h | --help>"
                )

    subparsers = parser.add_subparsers(
                     title       = "Commands",
                     dest        = "command",
                     description = "You can get additional help on these commands by typing\n `markouli [command] -h`.",
                     metavar     = "text - parse standard markdown text into patchouli's format"
                 )

    # parsing for just text, from text formatting 101
    argparseText = subparsers.add_parser(
                       "text",
                       description="plaintext parser",
                       prog=f"{parser.prog} text"
                   )
    argparseText.add_argument("source", help="source markdown file to convert")

    # finally, run the argument parser
    args = parser.parse_args()

    # run things based on our command)
    if (args.command == "text"):
        loader = MarkdownLoader()
        transformer = MarkdownASTTransfomer()
        
        ast = loader.fromFileToAST(args.source)
        patchouli = transformer.perform(ast)
        
        print("Debug output:")
        print(patchouli)

# bog standard python main guard
if (__name__ == "__main__"):
    main()