{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fe181231-2757-4237-8888-5ee526384143",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Looking in links: /usr/share/pip-wheels\n",
      "Requirement already satisfied: flask in /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages (2.2.2)\n",
      "Requirement already satisfied: Werkzeug>=2.2.2 in /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages (from flask) (2.2.3)\n",
      "Requirement already satisfied: Jinja2>=3.0 in /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages (from flask) (3.1.2)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages (from flask) (2.0.1)\n",
      "Requirement already satisfied: click>=8.0 in /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages (from flask) (8.0.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages (from Jinja2>=3.0->flask) (2.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de87e595-b466-4149-ad73-b6645e120d45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "from flask import render_template,request\n",
    "import json\n",
    "import time\n",
    "import requests\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "headers = {\n",
    "    \"Authorization\" : \"Token r8_0AxQUbuX68fMBhYnKFk6whir8HiMxH943p3FC\" ,\n",
    "    \"Content-Type\" : \"application/json\"\n",
    "}\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        q = request.form.get(\"question\")\n",
    "        print(q)\n",
    "        body = json.dumps(\n",
    "            {\n",
    "                \"version\" : \"db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf\",\n",
    "                \"input\" : {\n",
    "                    \"prompt\" : q\n",
    "                }\n",
    "            }\n",
    "        )\n",
    "        output = requests.post(\"https://api.replicate.com/v1/predictions\", data=body, headers=headers)\n",
    "        time.sleep(10)\n",
    "        get_url = output.json()[\"urls\"][\"get\"]\n",
    "        get_result = requests.post(get_url, headers=headers).json()[\"output\"]\n",
    "        \n",
    "        \n",
    "        return(render_template(\"index.html\",result=get_result[0]))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result=\"waiting......\"))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d96efc3-0843-4070-8839-2a8c87e63036",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
