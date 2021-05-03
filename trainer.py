{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "import joblib\n",
    "\n",
    "data=pd.read_csv('C:/Users/Inbasagar/Desktop/cricket and coding/preprocessing1.csv')\n",
    "\n",
    "venue_encoder= LabelEncoder()\n",
    "team_encoder=LabelEncoder()\n",
    "\n",
    "data['venue']=venue_encoder.fit_transform(data['venue'])\n",
    "data['batting_team']=venue_encoder.fit_transform(data['batting_team'])\n",
    "data['bowling_team']=venue_encoder.fit_transform(data['bowling_team'])\n",
    "\n",
    "anArray=data.to_numpy()\n",
    "\n",
    "X,y=anArray[:,:3],anArray[:,3]\n",
    "\n",
    "X=np.concatenate((np.eye(42)[anArray[:,0]],\n",
    "                      np.eye(2)[anArray[:,1]-1],\n",
    "                      np.eye(15)[anArray[:,2]],\n",
    "                      np.eye(15)[anArray[:,3]],\n",
    "                  ),axis=1)\n",
    "\n",
    "\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)\n",
    "\n",
    "linearRegressor=LinearRegression()\n",
    "linearRegressor.fit(X_train, y_train)\n",
    "\n",
    "joblib.dump(linearRegressor,'regression_model.joblib')\n",
    "\n",
    "joblib.dump(venue_encoder,'venue_encoder.joblib')\n",
    "\n",
    "joblib.dump(team_encoder,'team_encoder.joblib')\n",
    "\n",
    "print(linearRegressor.score(X_test,y_test))"
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
