{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Custom definitions and classes if any ###\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import joblib\n",
    "def predict_runs(input_test):\n",
    "    with open('regression_model.joblib','rb') as f:\n",
    "        regressor=joblib.load(f)\n",
    "    with open('venue_encoder.joblib','rb') as f:\n",
    "        venue_encoder=joblib.load(f)\n",
    "    with open('team_encoder.joblib','rb') as f:\n",
    "        team_encoder=joblib.load(f) \n",
    "        \n",
    "    test_case=pd.read_csv(input_test)\n",
    "\n",
    "    test_case['venue']=venue_enocder.transform(test_case['venue'])\n",
    "    test_case['batting_team']=team_encoder.transform(test_case['batting_team'])\n",
    "    test_case['bowling_team']=team_encoder.transform(test_case['bowling_team'])\n",
    "    \n",
    "    test_case=test_case[['venue','innings','batting_team','bowling_team']]\n",
    "    \n",
    "    testArray=test_case.to_numpy()\n",
    "    \n",
    "    test_case=np.concatenate((np.eye(42)[testArray[:,0]],\n",
    "                             np.eye(2)[testArray[:,1]-1],\n",
    "                             np.eye(15)[testArray[:,2]],\n",
    "                             np.eye(15)[testArray[:,3]],\n",
    "                             ),axis=1)\n",
    "    \n",
    "    print(test_case)\n",
    "    ### Your Code Here ###\n",
    "    return regressor.predict(test_case)\n",
    "    "
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
