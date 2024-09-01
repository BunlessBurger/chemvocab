import random

vocab = {
  "thermometer":"measures temperature",
  "test tube brush":"cleans test tubes, graduated cylenders, Erlenmeyer flasks",
  "iron ring":"support objects above a work surface or bunsen burner",
  "spot plate":"performing reactions with small amounts of chemicals",
  "rubber stopper":"sealing test tubes, flasks, and other laboratory glassware",
  "electronic balance":"measuring mass/weight",
  "heat glove":"protecting hands while picking up hot objects",
  "weigh boat":"weighing substances that will be transferredto another vessel",
  "test tube rack":"holds test tubes so they don't roll away, tip over, break",
  "spatula":"scraping, transferring, applying powders & past like chemicals",
  "graduated cylender":"measuring volume of liquids",
  "stir rod":"mixing & stirring liquids",
  "ring stand":"holding or clamping lab glassware & other equipment in place",
  "scoopula":"transferring powders & solids",
  "mortar & pestle":"crushing & grinding materials into fine paste or powder",
  "tongs":"grasping & lifting hot lab glass or ceramic dishes",
  "wash bottle":"cleaning lab glassware & other equipment",
  "test tube clamp":"holds a test tube in place when it's hot or shouldn't be touched",
  "goggles":"prevents particles, water, chemicals from striking the eye",
  "Erlenmeyer flask":"mixing, storing, holding liquids",
  "bunsen burner":"heating, sterilization, & combustion",
  "micropipet":"measureing & transferring small volumes of liquid",
  "watch glass":"evaporating liquid, heating a small amount of substance, cover",
  "test tube":"holding, mixing, heating chemical experiments",
  "beaker":"storing, mixing, heating liquid",
  "funnel":"pouring liquid or fine grained substances in container with small opening",
}

def askdef():
  word=random.choice(list(vocab.keys()))
  print(word)
  ans=input()
  print("-- ", vocab.get(word))
  print("")
  askdef()

def askvocab():
  word=random.choice(list(vocab.values()))
  print(word)
  ans=input()
  print("-- ", vocab.get(ans))
  print("")
  askvocab()


askdef()
#askvocab()