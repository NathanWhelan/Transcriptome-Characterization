#!/usr/bin/python

#########################################################################################################################
#This script was written by Nathan Whelan.  

# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF 
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE 
# SOFTWARE.
##########################################################################################################################
####THE INPUTS FOR THIS SCRIPT ARE A TAB DELIMITED TRINOTATE REPORT  AND A NAME FOR THE OUTPUT FILE!!!

#This program takes the GO Terms column from a Trinotate report and places it in a format that can be used by the WEGO web
#server http://wego.genomics.org.cn 

from __future__ import division
import re
import sys

if len(sys.argv) != 3:
	print "error! Please enter the input and output file"
	exit()
openFile=sys.argv[1]
outputFile=sys.argv[2]
goTermsFile = open(openFile)

regex = re.compile("GO:\d\d\d\d\d\d\d",re.MULTILINE)

output=open(outputFile,"w")
t=1
for x in goTermsFile:
    columnList=x.split("\t")
    goTermsList=regex.findall(columnList[11]) ##This is the column with GO terms. If for some reason your trinotate file is different, change
    preface="Sample" + str(t)
    if goTermsList !=[]:
        output.write(preface + "\t")
    for y in goTermsList:
        output.write(y + "\t")
    if goTermsList !=[]:
        output.write("\n")    
    t=t+1        
output.close()





