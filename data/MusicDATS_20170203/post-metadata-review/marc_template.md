Bibliographic template for stubs.

These need to be reviewed by original cataloging & batch.

Music DAT bib stub generation here includes:

- Creating this bibs for the analog _then also the digitized (tbd)_ (only the analog have barcodes)
- Add holdings for analog materials with the assigned local call number and part numbers
- Add item record(s) for each part with the assigned barcodes
- Suppress all of the above, flag for no updates/checks by Batch
- Pass list of record bib ids (we can generate post-batch report) back to Metadata

Things we need to check:

- call number location
- use of RDA-ish
- combine or not analog + digital records here
- location (Music library location? Non circulation/behind circ desk location?)


```
=LDR  01947njm a22004452i 4500
=001  [auto-generated]
=003  NIC
=007  ss\zunuuuipned
=008  170403sYYYY\\\\nyu\\uu\\\\\\\\\\\n\zxx\d
=040  \\$aNIC$beng$erda$dNIC
=035  \\$a[TBD]
=090  \\$a[CALL NUMBER]
=049  \\$aMAIN
=100  1\$a[NAME]
=245  10$a[TITLE] /$c[NAME].
=264  \0$c[YYYY].
=300  \\$a[PART MAX] audiocassette[S] :$bdigital ;$c2 7/8 x 2 1/8 in., 3/16 in. tape.
=336  \\$aperformed music$bprm$2rdacontent
=337  \\$aaudio$bs$2rdamedia
=338  \\$aaudiocassette$bss$2rdacarrier
=500  \\$aDigital audio tape.
=710  2_$a Music Library Recital DATs.
=710  2_$a Cornell University. $b Music Library.
=899  \\$a CULARMusicDAT
=852  81$aNIC$b[Music?]$c[Music Circ Desk?]$h[CALL NUMBER]
```
