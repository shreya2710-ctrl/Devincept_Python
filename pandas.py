{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         0\n",
      "0    Paris\n",
      "1       is\n",
      "2      the\n",
      "3  capital\n",
      "4       of\n",
      "5   France\n"
     ]
    }
   ],
   "source": [
    "lst = ['Paris', 'is', 'the', 'capital', 'of', 'France']\n",
    "df = pd.DataFrame(lst)\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    g\n",
      "1    o\n",
      "2    o\n",
      "3    g\n",
      "4    l\n",
      "5    e\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "data = np.array(['g', 'o', 'o', 'g', 'l', 'e', 'i', 's', 't', 'h', 'e', 'b', 'e', 's', 't'])\n",
    "ser = pd.Series(data)\n",
    "print(ser[:6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a    1\n",
      "b    2\n",
      "c    3\n",
      "d    4\n",
      "e    5\n",
      "dtype: int64 \n",
      "\n",
      " a    10\n",
      "b    20\n",
      "c    30\n",
      "d    40\n",
      "e    50\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])\n",
    " \n",
    "data1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])\n",
    " \n",
    "print(data, \"\\n\\n\", data1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Student_Name  Marks\n",
      "0        Rahul     43\n",
      "1         Abhi     22\n",
      "2       Kanika     49\n",
      "3        Preet     20\n",
      "4         Pari     39\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    " \n",
    "data = {'Student_Name':['Rahul', 'Abhi', 'Kanika', 'Preet', 'Pari'], 'Marks':[43, 22, 49, 20, 39]}\n",
    " \n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
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
       "      <th>Kanika_marks</th>\n",
       "      <th>Payal_Marks</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>100</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>90</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>85</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>95</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Kanika_marks  Payal_Marks\n",
       "0           100           30\n",
       "1            90           20\n",
       "2            85           45\n",
       "3            95           50"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    " \n",
    "dict = {'Kanika_marks':[100, 90, 85, 95], 'Payal_Marks' : [30, 20, 45, 50]}\n",
    " \n",
    "dataframe = pd.DataFrame(dict) \n",
    "dataframe"
   ]
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
