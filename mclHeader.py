#!/usr/bin/python

from __future__ import division
import re
import sys

#########################################################################################################################3
#This script was written by Nathan Whelan.  

# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF 
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE 
# SOFTWARE.

#This program takes a file with only the fasta headers from a transcript (or genome) assembly, a short name for 
#the transcriptome (e.g. if it is the human transcriptome a name might be "HUM") file, and the outputFile name (e.g. HumanMCLPrep.txt
#to be written.  

#It will output a file that can be concatenated for an MCL file.Please note that each name should be 
#unique for each taxon put through this script. It is assumed the output from this script for multiple taxa will be 
#concatenated for an MCL analysis







if len(sys.argv) != 4:
	print "Error.  There should be three inputs. A transcriptFile, a short name for the second columnd of MCL and the name for the output file"
	quit()

def header(transFile):
	headers=""	
	headFunctOutput=open("tmp.txt","w")	
	for line in open(transFile):
				
		if ">" in line:		
			headFunctOutput.write(line)
	headFunctOutput.close()

header(sys.argv[1])
transcript=sys.argv[2]


output=open(sys.argv[3],"w")
for x in open("tmp.txt"):
	regexTMP=re.compile("([^>\s]+)")
	regex1=regexTMP.search(x)
	r1=regexTMP.findall(x)	
	regexTMP=re.compile("([0-9]+)")
	r2=regexTMP.findall(r1[1])
	output.write(r1[0] + "\t" + transcript + "\t" + str(r2[0]) + "\n")
output.close()
