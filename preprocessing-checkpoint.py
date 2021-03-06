{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>venue</th>\n",
       "      <th>innings</th>\n",
       "      <th>batting_team</th>\n",
       "      <th>bowling_team</th>\n",
       "      <th>total_runs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>1</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>2</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Punjab Cricket Association Stadium, Mohali</td>\n",
       "      <td>1</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Punjab Cricket Association Stadium, Mohali</td>\n",
       "      <td>2</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Feroz Shah Kotla</td>\n",
       "      <td>1</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "      <td>Delhi Daredevils</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1631</th>\n",
       "      <td>MA Chidambaram Stadium, Chepauk, Chennai</td>\n",
       "      <td>2</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1632</th>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>1</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1633</th>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>2</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1634</th>\n",
       "      <td>MA Chidambaram Stadium, Chepauk, Chennai</td>\n",
       "      <td>1</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1635</th>\n",
       "      <td>MA Chidambaram Stadium, Chepauk, Chennai</td>\n",
       "      <td>2</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1636 rows ?? 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                           venue  innings  \\\n",
       "0                          M Chinnaswamy Stadium        1   \n",
       "1                          M Chinnaswamy Stadium        2   \n",
       "2     Punjab Cricket Association Stadium, Mohali        1   \n",
       "3     Punjab Cricket Association Stadium, Mohali        2   \n",
       "4                               Feroz Shah Kotla        1   \n",
       "...                                          ...      ...   \n",
       "1631    MA Chidambaram Stadium, Chepauk, Chennai        2   \n",
       "1632                    Wankhede Stadium, Mumbai        1   \n",
       "1633                    Wankhede Stadium, Mumbai        2   \n",
       "1634    MA Chidambaram Stadium, Chepauk, Chennai        1   \n",
       "1635    MA Chidambaram Stadium, Chepauk, Chennai        2   \n",
       "\n",
       "                     batting_team                 bowling_team  total_runs  \n",
       "0           Kolkata Knight Riders  Royal Challengers Bangalore          61  \n",
       "1     Royal Challengers Bangalore        Kolkata Knight Riders          26  \n",
       "2             Chennai Super Kings              Kings XI Punjab          53  \n",
       "3                 Kings XI Punjab          Chennai Super Kings          56  \n",
       "4                Rajasthan Royals             Delhi Daredevils          40  \n",
       "...                           ...                          ...         ...  \n",
       "1631  Royal Challengers Bangalore               Mumbai Indians          46  \n",
       "1632          Chennai Super Kings               Delhi Capitals          33  \n",
       "1633               Delhi Capitals          Chennai Super Kings          65  \n",
       "1634        Kolkata Knight Riders          Sunrisers Hyderabad          50  \n",
       "1635          Sunrisers Hyderabad        Kolkata Knight Riders          35  \n",
       "\n",
       "[1636 rows x 5 columns]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "\n",
    "ipl_data=pd.read_csv('.//ipl_csv2//all_matches.csv')\n",
    "\n",
    "relevantcolumns =['match_id','venue','innings','ball','batting_team','bowling_team','striker','non_striker','bowler','runs_off_bat','extras','wides','noballs','byes','legbyes','penalty']\n",
    "ipl_data=ipl_data[relevantcolumns]\n",
    "\n",
    "ipl_data['total_runs']=ipl_data['runs_off_bat']+ipl_data['extras']\n",
    "ipl_data=ipl_data.drop(columns=['runs_off_bat','extras'])\n",
    "ipl_data=ipl_data[ipl_data['ball']<=5.6]\n",
    "ipl_data=ipl_data[ipl_data['innings']<=2]\n",
    "ipl_data= ipl_data.groupby(['match_id','venue','innings','batting_team','bowling_team']).total_runs.sum()\n",
    "ipl_data=ipl_data.reset_index()\n",
    "ipl_data=ipl_data.drop(columns=['match_id'])\n",
    "ipl_data.to_csv('C:/Users/Inbasagar/Desktop/cricket and coding/preprocessing1.csv',index=False)\n",
    "ipl_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
