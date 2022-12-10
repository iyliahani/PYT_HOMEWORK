{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b66c0669",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Forecast:\n",
    "    def __init__(self, location):\n",
    "        self.location=location\n",
    "        \n",
    "    def get_daily_high(self):\n",
    "        return max(one_day_of_hourly_temperatures)\n",
    "    \n",
    "    def get_daily_low(self):\n",
    "        return min(one_day_of_hourly_temperatures)\n",
    "    \n",
    "    def get_daily_chance_of_rain(self):\n",
    "        number_of_years_of_data = 10\n",
    "        times_it_has_rained = 0\n",
    "        sum_rainfall = sum(one_day_of_hourly_temperatures,24)\n",
    "        if sum_rainfall > 0:\n",
    "            times_it_has_rained = times_it_has_rained + 1\n",
    "            return(get_daily_chance_of_rain)\n",
    "            \n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
