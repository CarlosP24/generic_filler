# generic_filler
Generic list and form filler for group activities with minors.
This code makes use of the package [docx-mailmerge](https://pypi.org/project/docx-mailmerge/) to write pretty authorizations and lists for group activities with minors.
It writhes them from easy to edit .docx templates and .csv files built from GoogleForms.
For each use of this code we just have to make sure that all fields in the GoogleForms and MailMerge fields in the .docx document are adequately referenced through the code (check "writers.py", "list_writers.py" and "renamers.py").

# REQUIREMENTS
Python packages:
    - json, pandas, mailmerge, yagmail
PDF writers:
    - libreoffice

# USAGE
1. Setup main data in "config.json". Databases (input_data and database) must be .csv files. Templates for authorizations and lists must be .docx with mail-merge fields as specified in "writers.py".
2. Set up the email text in "email_aux.py".
3. Set up "autorizacion.docx" with the data corresponding to the activity.
3. Set up "renamer.py", matching the fields in the input .csv (left, in Spanish) with the standard names in the pandas df (right, english)
4. Run "run_inscripciones.py" + SO (linux or macos). This script takes new data from "input_data" (from "last_time" onwards) and writes it in "database", fills the authorization and sends the confirmation email to the family.
5. Set up "groups.json", specifying center names and their responsible, with a contact.
6. Set up "template_list_x.docx" files with the data corresponding to the activity. MailMerge fields correspond to those in "list_writers.py".
7. Run "make_lists.py" to writhe .docx and .pdf lists of participants.
