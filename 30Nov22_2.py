{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9f6ce914",
   "metadata": {},
   "outputs": [],
   "source": [
    "employees = {'ID01' : {\"name\": \"Ron Swanson\", \"age\": 55, \"department\": \"Management\", \"phone\": \"555-1234\", \"salary\": \",000\"},\n",
    "            'ID02' :{\"name\": \"Leslie Knope\", \"department\": \"Middle Management\", \"phone\": \"555-4321\"},\n",
    "            'ID03' :{\"name\": \"Andy Dwyer\", \"department\": \" Shoe Shining\", \"phone\": \"555-1122\"},\n",
    "            'ID04' :{\"name\": \"April Ludgate\", \"department\": \"Administration\", \"phone\": \"555-3345\"}}\n",
    "             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8008c170",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ID01': {'name': 'Ron Swanson', 'age': 55, 'department': 'Management', 'phone': '555-1234', 'salary': ',000'}, 'ID02': {'name': 'Leslie Knope', 'department': 'Middle Management', 'phone': '555-4321'}, 'ID03': {'name': 'Andy Dwyer', 'department': ' Shoe Shining', 'phone': '555-1122'}, 'ID04': {'name': 'April Ludgate', 'department': 'Administration', 'phone': '555-3345'}}\n"
     ]
    }
   ],
   "source": [
    "print(employees)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e494d51d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Ron Swanson', 'age': 55, 'department': 'Management', 'phone': '555-1234', 'salary': ',000'}\n",
      "{'name': 'Leslie Knope', 'department': 'Middle Management', 'phone': '555-4321'}\n",
      "{'name': 'Andy Dwyer', 'department': ' Shoe Shining', 'phone': '555-1122'}\n",
      "{'name': 'April Ludgate', 'department': 'Administration', 'phone': '555-3345'}\n"
     ]
    }
   ],
   "source": [
    "for emp in employees:\n",
    "    print(employees[emp])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ef690da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1a2d25c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fcee4ff",
   "metadata": {},
   "outputs": [],
   "source": []
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
