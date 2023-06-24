import argparse
import doc_builder
import version_setter

def main():
    parser = argparse.ArgumentParser(description='Builds a word file from markdown documents')

    parser.add_argument('--InputDir', type=str, help='The directory where the novel project is', required=True)
    parser.add_argument('--Draft', type=int, help='The draft number')
    parser.add_argument('--Revision', type=int, help='The revision number')
    parser.add_argument('--NoVersion', action='store_true', help='If this is provided, the generated document will not be versioned')

    builder = doc_builder.Builder(version_setter.VersionSetter())


