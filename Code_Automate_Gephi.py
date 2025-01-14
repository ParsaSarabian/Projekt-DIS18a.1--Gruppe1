# movie_references.py

# TODO: catch error if entry is missing (e.g. Director)

import os
import pandas as pd

test = "AUS"      # test:= "EIN" oder "AUS" ("EIN": mit Zusatz-Infos in out_datei)
sep = ";"
nl = "\n"
movie_datei = "Unsere_Datei_movieID_serial.csv"
out_datei = os.path.splitext(movie_datei)[0] + "_ref.csv"
out_header = "Source;Target\n"

csv_out = open(out_datei, "w")
csv_out.write(out_header)

def write_record(ind_target):
  target = df['movieId'][ind_target]
  netto = str(row_movieId) + sep + str(target)     # row_movieId:= source
  #print("row_movieId: {}, target: {}".format(row_movieId, target))
  if row_movieId == target:                        # reflexiv
    return
  if test.upper() == "EIN":
    title =  df['Title'][ind_target]
    genre =  df['Genre'][ind_target]   
    director = df['Director'][ind_target]
    brutto = netto + "    # Target: [" + title + ", " + genre + ", " + director + "]"
  else:
    brutto = netto
  csv_out.write(brutto + nl)
  

# HEAD: movieId,Title,Genre,Director
df = pd.read_csv(movie_datei, sep = ',') # read csv-file into data frame
for ind in df.index:                     # Iterating over rows using index
  row_movieId = df['movieId'][ind]
  row_genre = df['Genre'][ind]
  row_director = df['Director'][ind]
  target_genre = df.query('Genre == ' + "\"" + row_genre + "\"")
  for item in target_genre.index:
    write_record(item)
  target_director = df.query('Director == ' + "\"" + row_director + "\"")
  for item in target_director.index:
    write_record(item)
csv_out.close()
