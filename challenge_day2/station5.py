team_mapping = {
    "Aya Abdelrahman": 5, "Bissola Adenekan": 1, "Shriya Agrawal": 5, "Ava Ali": 1,
    "Sean Almeida": 2, "Maja Arament": 2, "Gadis Arumcitta Gadis Masita": 3, 
    "Dorottya Báldy": 4, "Lotte Becking": 4, "Gabriella Beckley": 3, 
    "Alejandro Berges Coronel": 3, "Emma-Rose Blacher": 2, "Rasmus Blichfeldt": 1, 
    "Lumi Borgers": 5, "Christal Breinburg": 1, "Irene Bressanello": 2, "Anouk Buijs": 5, 
    "Volodymyr Butko": 4, "Catherin Catherin Andiani": 1, "Alva Chen": 4, "Roy Chen": 3, 
    "Nikko Chy": 3, "Ana Contreras Estrada": 2, "Walter Contreras Estrada": 5, 
    "Brendan Corcoran": 4, "Joeben Davis": 5, "Philine Dekker": 1, "Maria Dumitru": 5, 
    "Farah Elhusseini": 1, "Alexandru Enache": 2, "Wentao Fan": 3, 
    "Felicia Felicia Christy Leo": 3, "Jacco Friedeberg": 2, "Callum Ginsburg": 4, 
    "_mer Gökçe": 2, "Kimiya Gräfin Zu Eltz": 2, "mirre Grouls": 1, "Davide Hanna": 5, 
    "Leon Heemskerk": 5, "Micay van Hoogdalem": 3, "Andre Hua": 2, "Calson Huang": 5, 
    "Adam Humphreys": 1, "Elnara Ibrahimli": 3, "Angela Iversen": 4, "Mana Iwasaki": 3, 
    "Khushi Jain": 4, "Regina Jarillo Romo": 4, "Ilias Jelasity": 5, "Danielius Jonaitis": 4, 
    "Sophia Khinchikashvili": 5, "Scarlett Kim": 1, "Sina Kitapci": 3, "Anna Klinker": 5, 
    "Markus Knell": 5, "Maximilian Koch": 1, "Tadas Kraujalis": 3, "Akira Kuno": 4, 
    "Jamie Lee": 2, "Daniel Lefenda Lefenda": 3, "David Liebmann": 4, 
    "Noel Lilliestielke": 4, "Yujia Liu": 2, "Gabriela Mahecha Califa": 4, 
    "Rafael Mantoani": 1, "Josy Mertens": 1, "Kazuya Nagai": 4, "Lucas Nagtegaal": 5, 
    "Koyo Natsume": 2, "Alexia Nichifor": 3, "Viktor Nobel": 3, "Dasha Opoku-Gyamfi": 5, 
    "Clement Paitrault": 3, "Viggo Pauw": 2, "Thaïss Petit": 5, 
    "Diogo da Piedade Baptista": 3, "Gaspar Prieto Pote Monteiro Nogueira": 3, 
    "Abhijit Raghu": 1, "Asjfaaq Razab-Sekh": 4, "Alexandra Roskam": 3, 
    "Cem _ahingiray": 4, "Maria Sa_asi_ska": 1, "Federico Santi": 2, 
    "Nia Sas": 1, "Melody Scales": 2, "Bianka _ledzi_ska": 5, "Porter Stacy": 1, 
    "Nojus Stankevi_ius": 1, "Anna Szwedowska": 1, "Emilie Taffouraud": 5, 
    "Lucia Tanco Alonso": 2, "Mark Temchenko": 3, "Antonín Tesa_": 4, 
    "Niki Thrasyvoulou": 4, "Antonio Vasto": 4, "Merijn Vervoorn": 3, 
    "Juliette Visser": 2, "Bey Vongpatanasin": 5, "Weizhao Wang": 2, 
    "David Wild": 1, "Collins Woodbleach": 1, "Wu Ke Wu": 5, "Derrick Wyckelsma": 2, 
    "Sihun You": 3, "In Hyeok Youn": 2, "Shuting Yu": 4, "Marwan Zeinalabidin": 4, 
    "Meng Zhao": 1, "Fleming Ziehm": 5
}

def get_learning_team(name: str) -> int:
    """
    This function returns the learning team number of the given person.
    
    Parameters:
    name (str): The name of the person (case-insensitive).
    
    Returns:
    int: The learning team number of the person.
    
    Raises:
    ValueError: If the name is not found in the team mapping.
    """
    team_number = team_mapping.get(name, None)
    
    if team_number is None:
        raise ValueError(f"Name '{name}' not found in the team mapping.")
    
    return team_number