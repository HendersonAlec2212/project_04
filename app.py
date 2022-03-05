from asyncio import Event, events
from distutils.log import debug, set_verbosity
from sklearn import model_selection
from werkzeug.utils import secure_filename
import pandas as pd
import joblib
from flask import Flask, render_template, request, redirect, jsonify, make_response

app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET'])
def index():
    #home page for info and navigation
    return render_template("index.html")

@app.route("/sedan", methods=['POST', 'GET'])
def sedan():
    #form information to model to render 
    #accept the user selection and display
    sedan_pred =0

    sedan_model_dict = {
    # ML_model feature # - model name - model_ID
    '37' : ['300',1878.0],
    '38' : ['300C',25754.0],
    '39' : ['320i',2172.0],
    '40' : ['323i',13438.0],
    '41' : ['325i',1732.0],
    '42' : ['325xi',5195.0],
    '43' : ['328d',2220.0],
    '44' : ['328i',1709.0],
    '45' : ['328xi',2378.0],
    '46' : ['330e',2584.0],
    '47' : ['330i',1731.0],
    '48' : ['330xi',4308.0],
    '49' : ['335',14345.0],
    '50' : ['335d',1727.0],
    '51' : ['335i',1711.0],
    '52' : ['335xi',2357.0],
    '53' : ['340i',2231.0],
    '54' : ['428i',1870.0],
    '55' : ['430i',13798.0],
    '56' : ['435i',2230.0],
    '57' : ['440i',1729.0],
    '58' : ['525i',21790.0],
    '59' : ['525iA',2368.0],
    '60' : ['525xi',2313.0],
    '61' : ['528i',1715.0],
    '62' : ['528xi',2149.0],
    '63' : ['530e',1713.0],
    '64' : ['530i',2585.0],
    '65' : ['530iA',9115.0],
    '66' : ['530xi',2377.0],
    '67' : ['535d',2173.0],
    '68' : ['535i',1716.0],
    '69' : ['535i/535is',1688.0],
    '70' : ['535xi',2306.0],
    '71' : ['540i',24879.0],
    '72' : ['545i',8838.0],
    '73' : ['550i',1718.0],
    '74' : ['626',6093.0],
    '75' : ['640i',20813.0],
    '76' : ['640xi',2038.0],
    '77' : ['650i',2774.0],
    '78' : ['650i / ALPINA B6',1699.0],
    '79' : ['650i / B6',23521.0],
    '80' : ['740Li',8702.0],
    '81' : ['740i',2586.0],
    '82' : ['740iL',2240.0],
    '83' : ['745Li',1830.0],
    '84' : ['750Li',1723.0],
    '85' : ['750Li / ALPINA B7',21788.0],
    '86' : ['750Lxi',1721.0],
    '87' : ['750Lxi / ALPINA B7',21791.0],
    '88' : ['750i',1722.0],
    '89' : ['750i / ALPINA B7',13868.0],
    '90' : ['750i / B7',9569.0],
    '91' : ['750xi',16783.0],
    '92' : ['750xi / ALPINA B7',9568.0],
    '93' : ['A-Class',3151.0],
    '94' : ['A3',3676.0],
    '95' : ['A4',3146.0],
    '96' : ['A6',3148.0],
    '97' : ['A7',4015.0],
    '98' : ['A8',13827.0],
    '99' : ['ATS',1824.0],
    '100' : ['Accent',2773.0],
    '101' : ['Accord',1861.0],
    '102' : ['ActiveHybrid 5',2587.0],
    '103' : ['Alero',5063.0],
    '104' : ['Altima',1904.0],
    '105' : ['Amanti',2776.0],
    '106' : ['Arteon',9091.0],
    '107' : ['Aura',4336.0],
    '108' : ['Avalon',2465.0],
    '109' : ['Avenger',1892.0],
    '110' : ['Aveo',5880.0],
    '111' : ['Azera',26088.0],
    '112' : ['Bonneville',2307.0],
    '113' : ['Brooklands',20814.0],
    '114' : ['Brougham',8852.0],
    '115' : ['C-Class',2085.0],
    '116' : ['C-HR',2778.0],
    '117' : ['CC',8121.0],
    '118' : ['CLA-Class',2083.0],
    '119' : ['CLS-Class',2082.0],
    '120' : ['CT6',10297.0],
    '121' : ['CTS',1825.0],
    '122' : ['Cadenza',3071.0],
    '123' : ['Camry',2469.0],
    '124' : ['Caprice',8840.0],
    '125' : ['Caprice Police Vehicle',25134.0],
    '126' : ['Cavalier',3184.0],
    '127' : ['Challenger',1893.0],
    '128' : ['Charger',1895.0],
    '129' : ['Cirrus',5471.0],
    '130' : ['Civic',1863.0],
    '131' : ['Cobalt',4234.0],
    '132' : ['Concorde',4259.0],
    '133' : ['Concorde/LHS',14185.0],
    '134' : ['Continental',5192.0],
    '135' : ['Corolla',2208.0],
    '136' : ['Corolla Matrix',2466.0],
    '137' : ['Corsica',5181.0],
    '138' : ['Cougar',5191.0],
    '139' : ['Crown Victoria',21787.0],
    '140' : ['Cruze',1832.0],
    '141' : ['DTS',2764.0],
    '142' : ['Dart',2054.0],
    '143' : ['Deville',8844.0],
    '144' : ['E-Class',2081.0],
    '145' : ['ES',2475.0],
    '146' : ['Echo',5410.0],
    '147' : ['Elantra',2735.0],
    '148' : ['Equus',1903.0],
    '149' : ['Escort',3531.0],
    '150' : ['Fiesta',3267.0],
    '151' : ['Five Hundred',2347.0],
    '152' : ['Fleetwood',9122.0],
    '153' : ['Focus',1779.0],
    '154' : ['Forte',2462.0],
    '155' : ['Fusion',1780.0],
    '156' : ['G25',2358.0],
    '157' : ['G35',2305.0],
    '158' : ['G37',2337.0],
    '159' : ['G5',10997.0],
    '160' : ['G6',4263.0],
    '161' : ['G70',26481.0],
    '162' : ['G8',4264.0],
    '163' : ['G80',17213.0],
    '164' : ['G90',12580.0],
    '165' : ['GLI',5499.0],
    '166' : ['GS',2180.0],
    '167' : ['Genesis',1778.0],
    '168' : ['Geo Prizm',5875.0],
    '169' : ['Ghibli',11445.0],
    '170' : ['Giulia (952)',10326.0],
    '171' : ['Grand AM',9788.0],
    '172' : ['Grand Marquis',1792.0],
    '173' : ['Grand Prix',4262.0],
    '174' : ['HS',3185.0],
    '175' : ['I30',1720.0],
    '176' : ['I35',25871.0],
    '177' : ['ILX',2150.0],
    '178' : ['IS',2184.0],
    '179' : ['Impala',1833.0],
    '180' : ['Impala Limited',13634.0],
    '181' : ['Impreza',2235.0],
    '182' : ['Insight',2777.0],
    '183' : ['Integra',8842.0],
    '184' : ['Intrepid',3675.0],
    '185' : ['Ion',5879.0],
    '186' : ['Jetta',3137.0],
    '187' : ['K900',5347.0],
    '188' : ['L300',9822.0],
    '189' : ['LHS',5253.0],
    '190' : ['LS',2182.0],
    '191' : ['LS1',5343.0],
    '192' : ['LaCrosse',1821.0],
    '193' : ['LeSabre',3135.0],
    '194' : ['Legacy',2232.0],
    '195' : ['Lucerne',4267.0],
    '196' : ['M3',1710.0],
    '197' : ['M340i',13828.0],
    '198' : ['M35',1730.0],
    '199' : ['M35h',9452.0],
    '200' : ['M37',2376.0],
    '201' : ['M45',24944.0],
    '202' : ['M5',2024.0],
    '203' : ['M550i',3051.0],
    '204' : ['M56',2356.0],
    '205' : ['M6',2366.0],
    '206' : ['MKS',1794.0],
    '207' : ['MKZ',1790.0],
    '208' : ['Malibu',1834.0],
    '209' : ['Malibu Classic',1876.0],
    '210' : ['Marauder',6475.0],
    '211' : ['Mark',9787.0],
    '212' : ['Maxima',2302.0],
    '213' : ['Mazda3',2074.0],
    '214' : ['Mazda6',2078.0],
    '215' : ['Milan',1793.0],
    '216' : ['Mirage G4',13842.0],
    '217' : ['Montego',21792.0],
    '218' : ['Mulsanne',8475.0],
    '219' : ['Neon',8834.0],
    '220' : ['Ninety Eight (98)',3650.0],
    '221' : ['Optima',2739.0],
    '222' : ['PRIUS',2209.0],
    '223' : ['Panamera',7994.0],
    '224' : ['Passat',3134.0],
    '225' : ['Phaeton',6794.0],
    '226' : ['Protege',9116.0],
    '227' : ['Q50',1901.0],
    '228' : ['Q70',5813.0],
    '229' : ['Q70L',10208.0],
    '230' : ['Quattroporte',2367.0],
    '231' : ['RL',1872.0],
    '232' : ['RLX',12579.0],
    '233' : ['RS3',2765.0],
    '234' : ['RS4',2298.0],
    '235' : ['RS7',21793.0],
    '236' : ['Rapide',14175.0],
    '237' : ['Regal',1822.0],
    '238' : ['Rio',2299.0],
    '239' : ['S-Class',2086.0],
    '240' : ['S3',8173.0],
    '241' : ['S4',3147.0],
    '242' : ['S40',3127.0],
    '243' : ['S6',3677.0],
    '244' : ['S60',1959.0],
    '245' : ['S60 Cross Country',4781.0],
    '246' : ['S7',8258.0],
    '247' : ['S8',3678.0],
    '248' : ['S80',1960.0],
    '249' : ['S90',1728.0],
    '250' : ['SS',1837.0],
    '251' : ['STS',4300.0],
    '252' : ['SVX',8955.0],
    '253' : ['Sable',2365.0],
    '254' : ['Scion iA',13603.0],
    '255' : ['Sebring',1877.0],
    '256' : ['Sentra',1907.0],
    '257' : ['Seville',1828.0],
    '258' : ['Sonata',2459.0],
    '259' : ['Sonic',1835.0],
    '260' : ['Spectra',8685.0],
    '261' : ['Stratus',5500.0],
    '262' : ['TL',1873.0],
    '263' : ['TLX',5354.0],
    '264' : ['TSX',1874.0],
    '265' : ['Taurus',1782.0],
    '266' : ['Town Car',1791.0],
    '267' : ['Veloster',17528.0],
    '268' : ['Verano',1823.0],
    '269' : ['Versa',1894.0],
    '270' : ['WRX',2237.0],
    '271' : ['X-Type',2056.0],
    '272' : ['XE',11440.0],
    '273' : ['XF',2285.0],
    '274' : ['XJ',2242.0],
    '275' : ['XTS',1827.0],
    '276' : ['Yaris',2464.0],
    '277' : ['Yaris iA',24949.0],
    '278' : ['Zephyr',2771.0],
    '279' : ['new Passat',5878.0],}  

    if request.method=='POST':
        x=[]

        user_return = int(request.form.get("Model"))
        model_ID = sedan_model_dict[f'{user_return}'][1]
        x.append(model_ID)


        modelyear = int(request.form.get("inputYear"))
        print(modelyear)
        x.append(modelyear)
        
        mileage = int(request.form.get("inputMileage"))
        print(mileage)
        x.append(mileage)
        
        cylinders= float(request.form.get("cylinders"))
        print(cylinders)
        x.append(cylinders)
        
        make = int(request.form.get("Make"))
        print(make)
        makelist= [0]*34
        makelist[make]=1
        print(makelist)
        x.extend(makelist)
        
        model=int(request.form.get("Model"))
        modellist = [0]*242
        modellist[model]=1
        print(modellist)
        x.extend(modellist)

        gastype=int(request.form.get("gasoline"))
        print(gastype)
        x.append(gastype)

        print(x)

        model = joblib.load('./models/sedan_depth_7_81_no_color.joblib')
        sedan_pred= model.predict([x])
        print(f'sedan_pred = {sedan_pred}')
        sedan_pred= sedan_pred[0]
        sedan_pred = "${0:,.2f}".format(sedan_pred)

        print(sedan_pred) 
        return  render_template("sedan.html", sedan_pred=sedan_pred) 
    return render_template ("sedan.html")

@app.route("/truck")
def truck():
    #display drop down menu with states list
    #accept the user selection and display
    return render_template("truck.html")    

@app.route("/suv")
def suv():
    #display drop down menu with states list
    #accept the user selection and display 
    return render_template("suv.html")   

if __name__ == '__main__':
    app.run(debug=True)
