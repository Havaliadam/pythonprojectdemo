def convert_tr(text:str):
    characterSet={
      "ş":"s",
      "ı":"i",
      "ğ":"g",
      "ü":"u",
      "ç":"c",
      "ö":"o",
      "Ş":"S",
      "I":"I",
      "Ğ":"G",
      "Ü":"U",
      "Ç":"C",
      "Ö":"O"
    }
    text=list(text)
    for character in text:
        if character in characterSet:
            text[text.index(character)]=characterSet[character]

    return "".join(text)





print(convert_tr("Yaşamak dünyada en nadir şeydir. İnsanların büyük çoğunluğu var oluyorlar hepsi bu."))
