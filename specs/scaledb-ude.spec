%define __spec_install_pre /bin/true

Name:          scaledb-ude
Vendor:        ScaleDB, Inc. <info@scaledb.com>
Version:       16.04.01
Release:       P18863
BuildArch:     x86_64
Summary:       ScaleDB Cluster
License:       ScaleDB
Group: 	       database
URL:           http://www.scaledb.com

%define install_path	/usr/local

Prefix:        /usr/local
Conflicts:     mariadb-server, mysql-server
Requires:      libaio >= 0.3.109, nmap-ncat >= 1.105-7
AutoReqProv:   no



%description
High volume, high velocity transactional database engine
Distributed, clustered, always on. 
 

    
%pre
#!/bin/bash
#
# Copyright 2016 ScaleDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

set -e

SCALEDB_PACKAGE="scaledb-ude-16.04.01-P18863"
SCALEDB_PARENTDIR="/usr/local"
SCALEDB_BASEDIR="${SCALEDB_PARENTDIR}/${SCALEDB_PACKAGE}"
SCALEDB_LINK_BASEDIR="${SCALEDB_PARENTDIR}/scaledb"

SCALEDB_MARIADB_PACKAGE="scaledb-mariadb-16.04.01-10.1.13"
SCALEDB_MARIADB_PARENTDIR="${SCALEDB_PARENTDIR}"
SCALEDB_MARIADB_BASEDIR="${SCALEDB_MARIADB_PARENTDIR}/${SCALEDB_MARIADB_PACKAGE}"
SCALEDB_MARIADB_LINK_BASEDIR="${SCALEDB_MARIADB_PARENTDIR}/mysql"



# Show the license agreement
show_license() {

	# This is the main array containing the license agreement
	license=( [0]="" \
		  [1]="                        END USER SOFTWARE LICENSE AGREEMENT" \
		  [2]="" \
		  [3]="THIS SCALEDB SOFTWARE LICENSE AGREEMENT (\"AGREEMENT\") GOVERNS THE INSTALLATION" \
		  [4]="AND USE OF THE SCALEDB SOFTWARE DESCRIBED HEREIN." \
		  [5]="" \
		  [6]="YOU WILL BE REQUIRED TO INDICATE YOUR AGREEMENT TO THESE TERMS AND CONDITIONS IN" \
		  [7]="ORDER TO DOWNLOAD THE SOFTWARE, REGISTER THE SOFTWARE WITH SCALEDB AND/OR TO" \
	  	  [8]="INSTALL AND OPERATE THE SOFTWARE.  BY ANSWERING \"YES\" AT THE END OF THIS TEXT," \
		  [9]="OR BY INSTALLING THE SOFTWARE, OR USING ANY MEDIA THAT CONTAINS THE SOFTWARE," \
		 [10]="YOU ARE CONSENTING TO BE BOUND BY THIS AGREEMENT, INCLUDING ALL TERMS INCORPORATED" \
		 [11]="BY REFERENCE.  THIS AGREEMENT IS ENFORCEABLE AGAINST ANY PERSON OR ENTITY THAT USES" \
		 [11]="THE SOFTWARE AND ANY PERSON OR ENTITY THAT USES THE SOFTWARE ON ANOTHER PERSON'S" \
		 [12]="OR ENTITY'S BEHALF.  YOU AGREE THAT THIS AGREEMENT IS EQUIVALENT TO ANY WRITTEN" \
		 [13]="NEGOTIATED AGREEMENT SIGNED BY YOU.  IF YOU AGREE TO THESE TERMS ON BEHALF OF A" \
		 [14]="BUSINESS OR A GOVERNMENT AGENCY, DEPARTMENT OR INSTRUMENTALITY, YOU REPRESENT" \
		 [15]="AND WARRANT THAT YOU HAVE AUTHORITY TO BIND THAT BUSINESS TO THIS AGREEMENT, AND" \
		 [16]="YOUR AGREEMENT TO THESE TERMS WILL BE TREATED AS THE AGREEMENT OF THE BUSINESS." \
		 [17]="IN THAT EVENT, \"YOU\" AND \"YOUR\" REFER HEREIN TO THAT BUSINESS. THE TERMS OF" \
		 [18]="THIS AGREEMENT MAY BE UPDATED BY SCALEDB FROM TIME TO TIME." \
		 [19]="" \
		 [20]="" \
		 [21]="1.  DEFINITIONS." \
	         [22]="(a) \"Applications\" means computer software products that interface with the" \
	         [23]="    Software, either directly or through third-party software such as MySQL or" \
	         [24]="    MariaDB." \
	         [25]="(b) \"Excluded Causes\" means (a) any modification, reconfiguration, or" \
	         [26]="    maintenance of the Software performed by any party other than ScaleDB;" \
	         [27]="    (b) any use of the Software on a system that does not meet ScaleDB’s minimum" \
	         [28]="    standards for such Software, including use on a modified or unsupported" \
	         [29]="    operating system or environment (c) failure to implement all Updates issued" \
	         [30]="    by ScaleDB; (d) use of the Software in a manner for which it was not" \
	         [31]="    designed; and/or (e) accident, negligence, or misuse of the Software." \
	         [32]="(c) \"Software\" means the ScaleDB Version 10.15 software, in object code form," \
	         [33]="    plus any related documentation, scripts, or complementary applications and" \
	         [34]="    any subsequent software releases provided to You under this Agreement. " \
	         [35]="(d) \"Support\" means the then current support services offered by ScaleDB, as" \
	         [36]="    updated from time to time.." \
	         [37]="(e) \"Update\" means a new generally-released version of the Software designated," \
	         [38]="    in ScaleDB’s sole discretion, with a version number changed to the right or" \
	         [39]="    the left of the first decimal point." \
	         [40]="(f) \"You\", \"Your\" means the Licensee of Software and includes any person or" \
	         [41]="    entity where Software is operated and/or who use Software." \
		 [42]="" \
		 [43]="" \
	         [44]="2.  LICENSES." \
	         [45]="2.1 License to Software.  Subject to the terms and conditions of this Agreement," \
	         [46]="    ScaleDB grants to You a nonexclusive license to use Software solely for Your" \
	         [47]="    purposes. Use of Software beyond the above licensed uses shall be considered" \
	         [48]="    a material breach of this Agreement." \
	         [49]="2.2 Restrictions.  ScaleDB’s license grant is not transferable, assignable, or" \
	         [50]="    sublicenseable.   You shall not, nor shall You permit a third party to," \
	         [51]="    decompile, reverse engineer, or disassemble the Software’s source code or" \
	         [52]="    attempt to discover any portion of the source code or any trade secrets with" \
	         [53]="    respect to the Software. Further, You may not distribute or redistribute" \
	         [54]="    Software. Further, You shall not, nor shall You allow a third-party to," \
	         [55]="    combine, repackage, or bundle Software with any other software or hardware" \
	         [56]="    that violates the terms of the other software or hardware license. ScaleDB" \
	         [57]="    and its licensors retain all rights, title, and interest in and to all" \
	         [58]="    intellectual property rights embodied in, or associated with, the Software." \
	         [59]="    There are no implied licenses under this Agreement (by implication," \
	         [60]="    estoppel, or otherwise), and any rights not expressly granted to You under" \
	         [61]="    this Agreement are reserved by ScaleDB or its licensors." \
		 [62]="" \
		 [63]="" \
	         [64]="3.  WARRANTY AND DISCLAIMER." \
	         [65]="3.1 Performance Warranty.  ScaleDB does not warrant that operation of the" \
	         [66]="    Software will be uninterrupted, secure, or error free, or that all errors" \
	         [67]="    will be corrected.  ScaleDB further does not warrant that the information" \
	         [68]="    stored or transmitted by the Software is free from unauthorized" \
	         [69]="    modification." \
	         [70]="3.2 Disclaimer.  EXCEPT AS EXPRESSLY SET FORTH IN THIS SECTION 3, SCALEDB AND" \
	         [71]="    ITS LICENSORS DISCLAIM ALL OTHER WARRANTIES AND CONDITIONS, EXPRESS," \
	         [72]="    IMPLIED, OR STATUTORY, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES" \
	         [73]="    OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND" \
	         [74]="    NONINFRINGEMENT.  Each party acknowledges that it has not entered into this" \
	         [75]="    Agreement in reliance upon any warranty or representation except those" \
	         [76]="    specifically set forth herein." \
		 [77]="" \
		 [78]="" \
	         [79]="4.  TERM AND TERMINATION." \
	         [80]="4.1 Term.  This Agreement shall commence upon the Your approval of this" \
	         [81]="    Agreement, or the download or installation of Software, and shall continue" \
	         [82]="    in force until terminated.  By providing written notice, either party may" \
	         [83]="    terminate this Agreement upon the material breach of the other party of the" \
	         [84]="    terms of this Agreement, if such default continues for 30 days after written" \
	         [85]="    notice. " \
	         [86]="4.2 Effect of Termination.  Upon termination of this Agreement, all license" \
	         [87]="    rights granted under this Agreement immediately terminate, except as" \
	         [88]="    expressly specified otherwise. The provisions of Sections 1, 2.2, 3, 4.2," \
	         [89]="    5.2, 6, and 7 and Your obligation to pay any owed but unpaid amounts, shall" \
	         [90]="    survive the termination of this Agreement for any reason." \
		 [91]="" \
		 [92]="" \
	         [93]="5.  INDEMNITY." \
	         [94]="5.1 ScaleDB’s Indemnity.  ScaleDB may defend or settle any claims that You may" \
	         [95]="    incur that arise out of infringement by the Software of any copyright, trade" \
	         [96]="    secret, or U.S. patent right existing or issued as of the date that ScaleDB" \
	         [97]="    initially provided the applicable Software version or release.  ScaleDB may," \
	         [98]="    at its option and expense (in addition to fulfilling its indemnity" \
	         [99]="    obligations above): (a) replace the Software with substantially equivalent" \
	        [100]="    Software that could not reasonably infringe; (b) modify the Software so that" \
	        [101]="    it no longer could reasonably infringe but remains substantially equivalent;" \
	        [102]="    (c) obtain for You the right to continue its license rights to the Software;" \
	        [103]="    or (d) if none of the foregoing is reasonably available, terminate Your" \
	        [104]="    license to such Software.  ScaleDB will not be liable for claims based upon:" \
	        [105]="    (a) the use or combination of the Software with software, hardware, or other" \
	        [106]="    materials not provided by ScaleDB if infringement would not have occurred in" \
	        [107]="    the absence of such combination; (b) any marking or branding not applied by" \
	        [108]="    ScaleDB (or at the request of an authorized ScaleDB employee); or (c) any" \
	        [109]="    use of an altered or modified version of the Software if infringement would" \
	        [110]="    not have occurred but for the alteration or modification.  THIS SECTION" \
	        [111]="    STATES SCALEDB’S AND ITS LICENSORS’ SOLE AND EXCLUSIVE OBLIGATION WITH" \
	        [112]="    RESPECT TO INFRINGEMENT CLAIMS." \
	        [113]="5.2 Your Indemnity. You may defend or settle any claims which ScaleDB or its" \
	        [114]="    licensors may incur that arise out of the Applications (excluding the" \
	        [115]="    Software) or Your acts, omissions, misrepresentations, or failure to comply" \
	        [116]="    with applicable laws or regulations, and You shall indemnify ScaleDB and its" \
	        [117]="    licensors for all claims, losses, costs, damages, and expenses, including" \
	        [118]="    reasonable attorneys’ fees, attributable to any final judgment or settlement" \
	        [119]="    based on such claims. " \
	        [120]="5.3 Mechanics of Indemnity.  The foregoing indemnity obligations are conditioned" \
	        [121]="    on the party seeking indemnification (the \"Indemnified Party\"): (a) giving" \
	        [122]="    the proposed indemnifier (the \"Indemnifying Party\") notice of the relevant" \
	        [123]="    claim, (b) cooperating with the Indemnifying Party, at the Indemnifying" \
	        [124]="    Party’s expense, in the defense of such claim, and (c) giving the" \
	        [125]="    Indemnifying Party the right to control the defense and settlement of any" \
	        [126]="    such claim, except that the Indemnifying Party shall not enter into any" \
	        [127]="    settlement that affects the Indemnified Party’s rights or interest without" \
	        [128]="    the Indemnified Party’s prior written approval.  The Indemnified Party shall" \
	        [129]="    have the right to participate in the defense at its expense." \
		[130]="" \
		[131]="" \
	        [132]="6.  LIMITATIONS ON LIABILITY.  "
	        [133]="    EXCEPT WITH RESPECT TO ANY BREACHES OF SECTION 2 OR YOUR FAILURE TO COMPLY"
	        [134]="    WITH APPLICABLE LAWS OR REGULATIONS, IN NO EVENT SHALL EITHER PARTY (OR"
	        [135]="    SCALEDB’S LICENSORS) BE LIABLE FOR LOST PROFITS OR SPECIAL, INCIDENTAL, OR"
	        [136]="    CONSEQUENTIAL DAMAGES ARISING OUT OF OR IN CONNECTION WITH THIS AGREEMENT"
	        [137]="    (HOWEVER ARISING, INCLUDING NEGLIGENCE), EVEN IF SUCH PARTY HAS BEEN ADVISED"
	        [138]="    OF THE POSSIBILITY OF SUCH DAMAGES.  THIS LIMITATION OF LIABILITY SHALL"
	        [139]="    APPLY NOTWITHSTANDING THE FAILURE OF ESSENTIAL PURPOSE OF ANY LIMITED REMEDY"
	        [140]="    HEREIN.  "
	        [141]="    EXCEPT WITH RESPECT TO ANY BREACHES OF SECTION 2, OR YOUR FAILURE TO COMPLY"
	        [142]="    WITH APPLICABLE LAWS OR REGULATIONS, IN NO EVENT SHALL EITHER PARTY’S"
	        [143]="    LIABILITY RELATED TO THIS AGREEMENT EXCEED THE LICENSE FEES ACTUALLY PAID TO"
	        [144]="    SCALEDB BY YOU."
		[145]="" \
		[146]="" \
	        [147]="7.  GENERAL." \
	        [148]="7.1 Governing Law.  This Agreement will be governed by California law without" \
	        [149]="    regard to conflict of laws or principles.  Both parties submit to personal" \
	        [150]="    jurisdiction in California and agree that any cause of action arising under" \
	        [151]="    this Agreement must be brought in a federal or state court having within its" \
	        [152]="    venue San Mateo County, California." \
	        [153]="7.2 Assignment.  Neither party may assign its rights or delegate its duties" \
	        [154]="    under this Agreement without the other party’s prior written consent, except" \
	        [155]="    that a party may assign its rights and delegate its duties (in whole, but" \
	        [156]="    not in part) to an assignee who buys or is transferred all or substantially" \
	        [157]="    all the party’s assets or equity, unless the assignee is reasonably deemed a" \
	        [158]="    direct competitor of the other party.  Any attempted assignment or" \
	        [159]="    delegation in violation of the foregoing shall be void.  The parties’" \
	        [160]="    rights and obligations will bind and inure to the benefit of their" \
	        [161]="    respective successors and permitted assigns." \
	        [162]="7.3 Severability; Waiver.  If any provision of this Agreement is held to be" \
	        [163]="    invalid or unenforceable for any reason, the remaining provisions will" \
	        [164]="    continue in full force without being impaired or invalidated in any way." \
	        [165]="    The parties agree to replace any invalid provision with a valid provision" \
	        [166]="    which most closely approximates the intent and economic effect of the" \
	        [167]="    invalid provision.  The waiver by either party of a breach of any provision" \
	        [168]="    of this Agreement will not operate or be interpreted as a waiver of any" \
	        [169]="    other or subsequent breach." \
	        [170]="7.4 Force Majeure.  If performance of this Agreement, or any obligation under" \
	        [171]="    this Agreement (other than the making of payments), is interfered with by" \
	        [172]="    any act or condition beyond the reasonable control of the affected party," \
	        [173]="    the party so affected, upon giving prompt notice to the other party, will be" \
	        [174]="    excused from such performance to the extent of such condition." \
	        [175]="7.5 Government License.  If the License is being acquired by or on behalf of the" \
	        [176]="    U.S. Government or by a U.S. Government prime contractor or subcontractor" \
	        [177]="    (at any tier), in accordance with 48 C.F.R. 227.7202-4 (for Department of" \
	        [178]="    Defense acquisitions) and 48 C.F.R. 2.101 and 12.212 (for non-Department of" \
	        [179]="    Defense acquisitions), the government's rights in such code and any" \
	        [180]="    documentation, including its rights to use, modify, reproduce, release," \
	        [181]="    perform, display or disclose such code or documentation, will be subject in" \
	        [182]="    all respects to the license rights and restrictions provided in this" \
	        [183]="    Agreement." \
	        [184]="7.6 Independent Contractors.  The parties to this Agreement are independent" \
	        [185]="    contractors, and no agency, partnership, joint venture, or" \
	        [186]="    franchisor-franchisee relationship is intended or created by this Agreement." \
	        [187]="7.7 Notice.  Any notices required or permitted under this Agreement shall be" \
	        [188]="    given via the email address provided by You or at such other address as a" \
	        [189]="    You shall specify in writing.  Notice shall be deemed given within 8 hours" \
	        [190]="    of sending the appropriate email." \
	        [191]="7.8 Entire Agreement and Amendment.  This Agreement and any additional" \
	        [192]="    information referenced herein set forth the entire understanding and" \
	        [193]="    agreement of the parties, and supersede any and all oral or written" \
	        [194]="    agreements or understandings between the parties as to the subject matter of" \
	        [195]="    this Agreement. This Agreement shall control over any conflicting provisions" \
	        [196]="    of any purchase order or other similar business form, and such conflicting" \
	        [197]="    provisions are expressly rejected.  This Agreement may be updated by ScaleDB" \
	        [198]="    from time to time." \
	        [199]="" \
	        [200]="" \
		[201]="" )

	# Main case, it takes the request from the main block
	case "$1" in

		# Show all the EULA
		show)
			line_to_display=0
			while [ ${line_to_display} -le 201 ]
			do
				echo "${license[${line_to_display}]}"  >  /dev/tty
				line_to_display=$[${line_to_display}+1]
			done
			;;

		# Show the EULA in pages by 20 rows each
		page)
			clear screen >  /dev/tty
			
			# The current page (from 0 to 9)
			current_page=0

			# Keep scrolling until this is 0
			scroll_pages=1
			while [ ${scroll_pages} -eq 1 ]
			do
				line_to_display=$[${current_page}*20]
				bottom_row=$[${current_page}*20+19]

				# Must adjust the bottom
				if [ ${bottom_row} -gt 201 ]; then
					bottom_row=201
				fi

				echo "Page $[${current_page}+1]/10"  >  /dev/tty
				echo  >  /dev/tty

				# Inner loop, it prints the single lines in a page
				while [ ${line_to_display} -le ${bottom_row} ]
				do
					echo "${license[${line_to_display}]}"  >  /dev/tty
					line_to_display=$[${line_to_display}+1]
				done

				# Input from user (single character)
				echo  >  /dev/tty
				echo -n "(n)ext / (p)revious / (e)xit: "  >  /dev/tty
				read -n1 prompt_char  < /dev/tty
				echo  >  /dev/tty

				# Evaluate input
				case "${prompt_char}" in
					n)
						if [ ${current_page} -eq 9 ]; then
							# User hit Next but it is already at the bottom, so exit
							scroll_pages=0
						else
							# Increase page count
							current_page=$[${current_page}+1]
							clear screen >  /dev/tty
						fi
						;;
					p)
						if [ ${current_page} -gt 0 ]; then
							# Decrease page count
							current_page=$[${current_page}-1]
							clear screen >  /dev/tty
						fi
						;;
					e)
						# Exit
						scroll_pages=0
						;;
					*)
						;;
				esac
				echo >  /dev/tty
			done	
			;;
		*)
			echo "Unknown option." >  /dev/tty
			exit 1
			;;
	esac

}


echo    >  /dev/tty
echo "ScaleDB Universal Data Engine Installation"   >  /dev/tty
echo   >  /dev/tty
echo -n "Please press <Enter> to display the End User License Agreement or <CTRL-C> to exit."   >  /dev/tty
read continue_installation < /dev/tty
if [ "${continue_installation}" != "" ]; then
	exit 1
fi

echo >  /dev/tty
echo >  /dev/tty
echo "Please read carefully the following End User License Agreement" >  /dev/tty
echo >  /dev/tty
echo >  /dev/tty
show_license show

# Main loop
keep_asking="Y"
while [ "${keep_asking}" = "Y" ]
do
	echo "Options:" >  /dev/tty
	echo "  yes  : You accept the license" >  /dev/tty
	echo "  no   : You do not accept the license" >  /dev/tty
	echo "  page : Display the license page by page (20 rows per page)" >  /dev/tty
	echo "  show : Display the full license again" >  /dev/tty
	echo "  exit : Abort the installation" >  /dev/tty

	echo -n "Option [yes|no|page|show|exit]:" >  /dev/tty
	read accept_license < /dev/tty

	case $accept_license in
		yes)
			keep_asking="N"
			;;
		no)
			exit 1
			;;
		page)
			show_license page
			;;
		show)
			show_license show
			;;	
		exit)
			exit 1
			;;
		*)
			echo "Unrecognized answer." >  /dev/tty
			echo >  /dev/tty
			;;
	esac
done

# Disk space check
if [ "`df -Pk ${SCALEDB_PARENTDIR} | tail -1 |  awk '{print $4}'`" -lt "15000000" ]; then
	
	echo >  /dev/tty
	echo >  /dev/tty
	echo "Warning, insufficient disk space in ${SCALEDB_PARENTDIR}, min 15GB required." >  /dev/tty	
	echo -n "Please press <Enter> to continue or <CTRL-C> to exit."   >  /dev/tty

	read continue_installation < /dev/tty	
	if [ "${continue_installation}" != "" ]; then
		exit 1
	fi
fi


# Check if the scaledb dir link is already set
if [ -L "${SCALEDB_LINK_BASEDIR}" -o -f "${SCALEDB_LINK_BASEDIR}" ]; then
	echo
	echo "${SCALEDB_LINK_BASEDIR} is already set. Remove the folder or link and run the installation again."
	exit 1
fi

if [ "`grep -c '^scaledb:' /etc/group`" = "0" ]; then
				groupadd scaledb > /dev/null
        if [ "$?" != "0" ]; then
                echo "Error creating the scaledb group."
                exit 1
        fi
fi

if [ "`grep -c '^scaledb:' /etc/passwd`" = "0" ]; then
				adduser -g scaledb --comment "ScaleDB" --shell /bin/bash scaledb > /dev/null 

        # If the adduser has been OK, set the password
        if [ "$?" = "0" ]; then
                echo scaledb | passwd scaledb --stdin  > /dev/null
                if [ "$?" != "0" ]; then
                        echo "Error setting password for scaledb user."
                        exit 1
                fi
        else
                echo "Error creating the scaledb user."
                exit 1
        fi
fi

# Check and insert the new limit on open files for the scaledb user
sed -e '/scaledb/ s/^#*/#/' -i /etc/security/limits.conf
echo >> /etc/security/limits.conf
echo "# Added by the ScaleDB installer" >> /etc/security/limits.conf
echo "scaledb soft nofile 65536" >> /etc/security/limits.conf
echo "scaledb hard nofile 65536" >> /etc/security/limits.conf

exit $?

%post
#!/bin/sh
#
# Copyright 2016 ScaleDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

set -e

SCALEDB_PACKAGE="scaledb-ude-16.04.01-P18863"
SCALEDB_PARENTDIR="/usr/local"
SCALEDB_BASEDIR="${SCALEDB_PARENTDIR}/${SCALEDB_PACKAGE}"
SCALEDB_LINK_BASEDIR="${SCALEDB_PARENTDIR}/scaledb"

SCALEDB_MARIADB_PACKAGE="scaledb-mariadb-16.04.01-10.1.13"
SCALEDB_MARIADB_PARENTDIR="${SCALEDB_PARENTDIR}"
SCALEDB_MARIADB_BASEDIR="${SCALEDB_MARIADB_PARENTDIR}/${SCALEDB_MARIADB_PACKAGE}"
SCALEDB_MARIADB_LINK_BASEDIR="${SCALEDB_MARIADB_PARENTDIR}/mysql"




# Set the Base Dir
ln -s "${SCALEDB_BASEDIR}" "${SCALEDB_LINK_BASEDIR}"
if [ "$?" != "0" ]; then
        echo "Error setting the ${SCALEDB_LINK_BASEDIR} symbolic link."
        exit 1
fi

# Change the ownership of the files installed
chown -R scaledb:scaledb "${SCALEDB_BASEDIR}"
if [ "$?" != "0" ]; then
        echo "Error changing ownership of the ScaleDB base directory."
        exit 1
fi

chown -R scaledb:scaledb "${SCALEDB_LINK_BASEDIR}"
if [ "$?" != "0" ]; then
        echo "Error changing ownership of the ScaleDB symbolic link."
        exit 1
fi



# Copy and reconfigure the Library config file
cp  "${SCALEDB_BASEDIR}/etc/scaledblib.conf" "/etc/ld.so.conf.d/scaledblib.conf"
if [ "$?" != "0" ]; then
        echo "Error copying the library config file."
        exit 1
fi

ldconfig
if [ "$?" != "0" ]; then
        echo "Error configuring the shared object libraries."
        exit 1
fi


# Retrieve the home directory path for the scaledb user
scaledb_home_dir=`grep "^scaledb" /etc/passwd | cut -d: -f6`

# Work only if .bash_profile exists
if [ -f "${scaledb_home_dir}/.bash_profile" ]; then

	echo >> "${scaledb_home_dir}/.bash_profile"
	echo "# Added by the ScaleDB UDE package installer" >> "${scaledb_home_dir}/.bash_profile"

        # Setting the new path to ...scaledb/scripts for the scaledb user
        if  [ `grep -c "^\s*PATH=.*${SCALEDB_LINK_BASEDIR}/scripts" "${scaledb_home_dir}/.bash_profile"` -eq 0 ]; then
                echo "PATH=\"${SCALEDB_LINK_BASEDIR}/scripts:\${PATH}\"" >> "${scaledb_home_dir}/.bash_profile"
                echo  >> "${scaledb_home_dir}/.bash_profile"
        fi

	if [ `grep -c "^\s*cat.*profile_text" "${scaledb_home_dir}/.bash_profile"` -eq 0 ]; then
		echo "clear" >> "${scaledb_home_dir}/.bash_profile"
		echo "cat \"${SCALEDB_LINK_BASEDIR}/profile_text\"" >> "${scaledb_home_dir}/.bash_profile"
		echo  >> "${scaledb_home_dir}/.bash_profile"
	fi
fi

echo ""
echo "ScaleDB Universal Data Engine installation completed."
echo "You can control ScaleDB using the scaledb user. The default password is scaledb."
echo ""
 
exit $?

 
%preun 
#!/bin/sh
#
# Copyright 2016 ScaleDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

set -e

SCALEDB_PACKAGE="scaledb-ude-16.04.01-P18863"
SCALEDB_PARENTDIR="/usr/local"
SCALEDB_BASEDIR="${SCALEDB_PARENTDIR}/${SCALEDB_PACKAGE}"
SCALEDB_LINK_BASEDIR="${SCALEDB_PARENTDIR}/scaledb"

SCALEDB_MARIADB_PACKAGE="scaledb-mariadb-16.04.01-10.1.13"
SCALEDB_MARIADB_PARENTDIR="${SCALEDB_PARENTDIR}"
SCALEDB_MARIADB_BASEDIR="${SCALEDB_MARIADB_PARENTDIR}/${SCALEDB_MARIADB_PACKAGE}"
SCALEDB_MARIADB_LINK_BASEDIR="${SCALEDB_MARIADB_PARENTDIR}/mysql"

# Check and stop MariaDB Server
if [ -f "${SCALEDB_MARIADB_BASEDIR}/support-files/mysql.server" ]; then
	if [ `"${SCALEDB_MARIADB_BASEDIR}/support-files/mysql.server" status | tail -1 | grep -c "MySQL running"` -gt 0 ]; then
		echo -n "Stopping MariaDB Server..."
		"${SCALEDB_MARIADB_BASEDIR}/support-files/mysql.server" stop
		echo "Done."
	fi
fi

# Check and stop SLM
if [ -f "${SCALEDB_BASEDIR}/scripts/scaledb-slm" ]; then
        if [ `"${SCALEDB_BASEDIR}/scripts/scaledb-slm" status | tail -1 | grep -c "SLM is running"` -gt 0 ]; then
		echo -n "Stopping Cluster Manager..."
		"${SCALEDB_BASEDIR}/scripts/scaledb-slm" kill
		echo "Done."
	fi
fi

# Check and stop CAS
if [ -f "${SCALEDB_BASEDIR}/scripts/scaledb-cas" ]; then
        if [ `"${SCALEDB_BASEDIR}/scripts/scaledb-cas" status | tail -1 | grep -c "CAS is running"` -gt 0 ]; then
		echo -n "Stopping Storage node..."
		"${SCALEDB_BASEDIR}/scripts/scaledb-cas" kill
		echo "Done."
	fi
fi

# Remove Data, Logs, Temporary structures, Locks
echo -n "Removing data files..."
rm -rf ${SCALEDB_BASEDIR}/data/*
rm -rf ${SCALEDB_BASEDIR}/logs/*
rm -rf ${SCALEDB_BASEDIR}/locks/*
rm -rf ${SCALEDB_BASEDIR}/tmp/*
echo "Done."

# Remove the Base Dir link
rm -f ${SCALEDB_LINK_BASEDIR}


# Remove and reconfigure the ld config
rm -f /etc/ld.so.conf.d/scaledblib.conf
ldconfig

 
exit $?



%postun
#!/bin/sh
#
# Copyright 2016 ScaleDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

set -e

SCALEDB_PACKAGE="scaledb-ude-16.04.01-P18863"
SCALEDB_PARENTDIR="/usr/local"
SCALEDB_BASEDIR="${SCALEDB_PARENTDIR}/${SCALEDB_PACKAGE}"
SCALEDB_LINK_BASEDIR="${SCALEDB_PARENTDIR}/scaledb"


# Remove the ScaleDB directory, if it is in the usual position
if [ -d "${SCALEDB_BASEDIR}" ]
then
	rm -rf ${SCALEDB_BASEDIR}
fi


%files 
%{install_path}/*




 