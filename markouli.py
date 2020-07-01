import argparse

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

    print(args.command)

# bog standard python main guard
if (__name__ == "__main__"):
    main()
