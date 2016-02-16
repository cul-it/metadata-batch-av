#AV Digitization to eCommons Metadata Docs
*point person: [Christina](mailto:cmh329@cornell.edu)*

##Metadata Workflow
This section primarily focuses on where Metadata Services (in particular Christina) plays a role. Has end-to-end workflow as she understands it, for sake of clarification.

1. Selector chooses items to be digitized. Their list should contain preliminary MARC metadata for identification - titles, bib IDs, authors (MARC record extents - i.e., 2 tapes? could be helpful). The MARC-derived portions of the list may be checked/generated by Metadata Unit (Christina). That list should be reviewed/confirmed complete and appropriate for digitization/re-digitization by Hannah & Dianne.
2. List of items gets sent to Digitization Services. They perform their magic. The list of items, for Digitization, becomes a spreadsheet containing the following information for each file they generate: 
    3. **filename** (including extension or separate column with MIME type), accession number (the original bib id), 
    4. **title**,  
    5. **description/author**, 
    6. their digitization notes. 
Once digitization is complete, this goes to Hannah &/or Dianne.
3. The digitized items get loaded into Kaltura using the information in the digitization spreadsheet. I'm not sure if Hannah or Mira (or somebody else) handles this. From this is generated a post-Kaltura spreadsheet that has: 
    4. **filename** (including extension or separate column with MIME type), 
    5. **accession number** (the original bib id), 
    6. **title**,  
    7. **description/author**, 
    8. **ID number** (I think this is the filename), 
    9. **Kaltura ID** (this is I think used by the embed code/viewer code).
4. The post-Kaltura spreadsheet gets passed to Christina for metadata enhancement using the original MARC records. This involves:
    5. Creating eCommons Ingest spreadsheet, where rows go from 1 per digitization file to 1 per MARC bibliographic record ID. *Combined cells currently use a '|' for the delimiter. Can also be broken into repeated columns. Up to Mira's preference.*
    6. Pulling MARC records for all the related bibliographic records from Voyager (accessionNumber entries, now the spreadsheet row index). This is stored in MARCXML.
    6. Crosswalking the MARC records retrieved to the metadata mapping for eCommons as discussed below in the Metadata Mapping section.
    7. Adding fields that are constants across these records but aren't derived from the MARC records (see Metadata Mapping section).
    8. Perform normalization and enhancement - clean up punctuation, normalize controlled headings, get date encodings correct, check crosswalk.
9. eCommons Ingest spreadsheet gets sent to Mira, who then performs eCommons ingest of these records and related files.

Outstanding metadata questions:

* Want to add some fields to eCommons for this? Thinking dc.contributor.speaker, dc.subject.fast in particular. Right now, FAST headings get dumped in preference for keeping more specific dc.subject.lcsh.
* This mapping works with all the metadata fields currently configured in eCommons - some of these fields are not currently used, so uncertain of their display. Will need to pass the mapping to Mira or possibly George for review on this front?
* Want to eventually pull the eCommons handles for these items into the originating MARC records as 856 41s? Will need to discuss with Pam.

##Tracking & Functional Requirements

At present, it's down to receiving a file from Hannah and passing to Mira. Waiting to see what tracking system is used for these workflows. 

For metadata portion, I need a spreadsheet that relates digitization objects (filenames, kaltura IDs) to MARC Bibliographic Record identifiers, if nothing else.

##Metadata Mapping

For the eCommons Ingest spreadsheet/dataset. Source desribes where the field should have been added to the dataset (see workflow steps above).

Source | Post-Kaltura Data | eCommons Fields | MARC Metadata | Notes
---|---|---|---|---
Digitization | ID Number | dc.description.audio | n/a | filenames? eCommons dc.description.audio has scope note 'Entry ID for kaltura audio files'
Digitization? | Kaltura ID | dc.description.viewer | n/a | entry id for Kaltura viewer? eCommons dc.description.viewer has scope note 'Entry ID for Kaltura Viewer'
Selector? | Title | dc.title | 245abp | Clean up punctuation, remove $h qualifiers, if present.
Selector? | Description | *dc.contributor.author* | *100, 700* | At least in starting sheet, this column competely maps to author, not general description note or more specific description abstract. Will be asking about 1. changing this in future spreadsheets 2. getting eCommons field 'dc.contributor.speaker' added.
Selector? | Accession Number | dc.relation.isFormatOf | 001 | MARC Bibliographic record identifier. Consider generating URL from this for linking to record as appears in Blacklight interface. Could also be used later for generating eCommons URLs to add to MARC records.
Crosswalk | n/a | dc.date.copyright | n/a (possibly 260c/264c) | Will we be adding any rights information to these?
Crosswalk | n/a | dc.date.created | LDR/008 pos 7-10 (possibly 260c/264c) | Make sure is EDTF Encoding. Don't think these MARC records generally have 260/264c fields. 
Crosswalk | n/a | dc.description.abstract | 520 3# a | Probably will include 520 generally, 500s too possibly.
Crosswalk | n/a | dc.description.tableOfContents | 505 * | Will need normalization review if even included for these records.
Crosswalk | n/a | dc.description | 500 *, 518, not specified 5XX, not 500 that begins with 'Duration: ' | will need to be reviewed for item- and format-specific notes.
Crosswalk | n/a | dc.format.extent | 500 that begins with 'Duration: '. Not the 300 field - this is for the physical object. | Possibly will get this information also from the Digitization work.
Digitization or Crosswalk | MimeType or Filename | dc.format.mimetype | n/a | Derived from Digitization work and filenames.
Crosswalk | n/a | dc.language.iso | LDR/008 pos 35-37 (possibly 041) | Convert to ISO 639-2 for now. eCommons seems to try to use that.
Crosswalk | n/a | dc.relation.requires | n/a | Any constant notes on the required software to listen?
Crosswalk | n/a | dc.rights | n/a | May want to add later.
Crosswalk | n/a | dc.subject.ddc | 082 | Don't think this displays currently in eCommons.
Crosswalk | n/a | dc.subject.lcc | 050 #4 | Don't think this displays currently in eCommons. Want to include Cutter?
Crosswalk | n/a | dc.subject.lcsh | 600, 610, 650 #0 | Will need normalization. Don't include FAST headings here for now.
Crosswalk | n/a | dc.subject.mesh | 600, 610, 650 #2 | Will need normalization.
Crosswalk | n/a | dc.subject | 600, 610, 650 #7 | Include Fast headings here that aren't repeating LCSH headings.
Crosswalk | n/a | dc.title.alternative | 246, 240, 830. | Normalize. Want to use dct:isPartOf?
Crosswalk | n/a | dc.type | n/a | always will be 'Sound'



