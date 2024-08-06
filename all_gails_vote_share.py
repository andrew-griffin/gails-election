import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read election results
df = pd.read_csv("HoC-GE2024-results-by-constituency.csv", header=0, thousands=',')

df['Lab'] = df['Lab'].astype(float)
df['Con'] = df['Con'].astype(float)
df['LD'] = df['LD'].astype(float)
df['RUK'] = df['RUK'].astype(float)
df['Green'] = df['Green'].astype(float)
df['SNP'] = df['SNP'].astype(float)
df['Valid votes'] = df['Valid votes'].astype(float)

lab_vote = df['Lab']
con_vote = df['Con']
lib_dem_vote = df['LD']
reform_vote = df['RUK']
green_vote = df['Green']
snp_vote = df['SNP']
total_vote = df['Valid votes']

# Read postcodes of all Gails stores
gails_list = pd.read_csv('all_gails.csv', header=0)
gails_postcodes = gails_list.iloc[:,0]

# Read all locations
all_places = pd.read_csv('pcd_pcon_uk_lu_may_24.csv')
all_postcodes = all_places['pcd']
all_constituencies = all_places['pconnm']

# Find list of constituencies with Gails in
GCs = []
for j in range(len(gails_postcodes)):
    var1 = all_constituencies[all_postcodes == gails_postcodes[j]]
    GCs = np.append(GCs, var1)

# Deduplicate list
gails_constituencies = []
for i in GCs:
    if i not in gails_constituencies:
        gails_constituencies.append(i)

print(len(gails_constituencies))


# Calculate election numbers for Gail's constituencies
gails = np.isin(df['Constituency name'], gails_constituencies)
gails_lab_vote = lab_vote[gails]
gails_con_vote = con_vote[gails]
gails_lib_dem_vote = lib_dem_vote[gails]
gails_reform_vote = reform_vote[gails]
gails_green_vote = green_vote[gails]
gails_snp_vote = snp_vote[gails]
gails_total_vote = total_vote[gails]

# Total vote share
lab_vote_share = np.sum(lab_vote)*100/np.sum(total_vote)
con_vote_share = np.sum(con_vote)*100/np.sum(total_vote)
lib_dem_vote_share = np.sum(lib_dem_vote)*100/np.sum(total_vote)
reform_vote_share = np.sum(reform_vote)*100/np.sum(total_vote)
green_vote_share = np.sum(green_vote)*100/np.sum(total_vote)
snp_vote_share = np.sum(snp_vote)*100/np.sum(total_vote)

# Vote share in Gail's constituencies
gails_lab_vote_share = np.sum(lab_vote[gails])*100/np.sum(total_vote[gails])
gails_con_vote_share = np.sum(con_vote[gails])*100/np.sum(total_vote[gails])
gails_lib_dem_vote_share = np.sum(lib_dem_vote[gails])*100/np.sum(total_vote[gails])
gails_reform_vote_share = np.sum(reform_vote[gails])*100/np.sum(total_vote[gails])
gails_green_vote_share = np.sum(green_vote[gails])*100/np.sum(total_vote[gails])
gails_snp_vote_share = np.sum(snp_vote[gails])*100/np.sum(total_vote[gails])

# Plot
party_list = ["Lab", "Lab (G)", "Con", "Con (G)", "LD", "LD (G)", "Reform", "Reform (G)", "Green", "Green (G)", "SNP", "SNP (G)"]
value_list = [lab_vote_share, gails_lab_vote_share, con_vote_share, gails_con_vote_share, lib_dem_vote_share, gails_lib_dem_vote_share, reform_vote_share, gails_reform_vote_share, green_vote_share, gails_green_vote_share, snp_vote_share, gails_snp_vote_share]

print(value_list)

colour_list = ['r', 'r', 'b', 'b', 'orange', 'orange', 'lightblue', 'lightblue', 'g', 'g', 'y', 'y']
plt.bar(party_list, value_list, color=colour_list)
plt.ylabel('Vote share (%)')

plt.minorticks_on()
plt.tick_params(axis='y',which='major',right='off')
plt.tick_params(axis='y',which='minor',right='off')
plt.tick_params(axis='x', which='minor', bottom=False)
plt.xticks(rotation=30)

plt.show()
