#!/usr/bin/python  
import urllib2,htmllib,formatter

page=urllib2.urlopen('file:///Users/zxwxfczxx/Desktop/soufun_proje_list_all.html').read()

def extract_text( html) :
    # Derive from formatter.AbstractWriter to store paragraphs.
    writer = LineWriter()
    # Default formatter sends commands to our writer.
    formatter = AbstractFormatter( writer)
    # Derive from htmllib.HTMLParser to track parsed bytes.
    parser = TrackingParser( writer, formatter )
    # Give the parser the raw HTML data.
    parser .feed( page)
    parser .close()
    # Filter the paragraphs stored and output them.
    return writer.output()
class TrackingParser( htmllib .HTMLParser ) :
    """Try to keep accurate pointer of parsing location."""
    def __init__ ( self , writer, *args) :
        htmllib .HTMLParser .__init__ ( self , *args)
        self .writer = writer
    def parse_starttag( self , i) :
        index = htmllib .HTMLParser .parse_starttag( self , i)
        self .writer .index = index
        return index
    def parse_endtag( self , i) :
        self .writer .index = i
        return htmllib .HTMLParser .parse_endtag( self , i)
class Paragraph:
    def __init__ ( self ) :
        self .text = ''
        self .bytes = 0
        self .density = 0.0
class LineWriter( formatter .AbstractWriter) :
    def __init__ ( self , *args) :
        self .last_index = 0
        self .lines = [ Paragraph()]
        formatter .AbstractWriter .__init__ ( self )
    def send_flowing_data( self , data) :
        # Work out the length of this text chunk.
        t = len ( data)
        # We've parsed more text, so increment index.
        self .index += t
        # Calculate the number of bytes since last time.
        b = self .index - self .last_index
        self .last_index = self .index
        # Accumulate this information in current line.
        l = self .lines[ -1 ]
        l.text += data
        l.bytes += b
    def send_paragraph( self , blankline) :
        """Create a new paragraph if necessary."""
        if self .lines[ -1 ] .text == '' :
            return
        self .lines[ -1 ] .text += 'n' * ( blankline+1 )
        self .lines[ -1 ] .bytes += 2 * ( blankline+1 )
        self .lines .append( Writer.Paragraph())
    def send_literal_data( self , data) :
        self .send_flowing_data( data)
        print data
    def send_line_break( self ) :
        self .send_paragraph( 0 )

    
