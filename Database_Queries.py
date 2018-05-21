def summary_graphs(age, metric):

    import sqlite3
    connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
    # cursor = connection.execute("select genotype from Neurons")
    # for row in cursor:
    #     print row

    #By Genotype and Condition
    WTTR = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '"+age+"'and genotype='WT' and condition='TR'")
    WTTR_values = [row[0] for row in WTTR]
    # print WTTR_values

    WTDD = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='WT' and condition='DD'")
    WTDD_values = [row[0] for row in WTDD]
    # print WTDD_values

    KOTR = connection.execute("select "+metric+ " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '"+age+"'and genotype='KO' and condition='TR'")
    KOTR_values = [row[0] for row in KOTR]
    # print KOTR_values

    KODD = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='KO' and condition='DD'")
    KODD_values = [row[0] for row in KODD]
    # print KODD_values


    #By Genotype, Condition, and Sex
    WTTRM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='WT' and condition='TR' and sex='M'")
    WTTRM_values = [row[0] for row in WTTRM]
    # print WTTRM_values
    WTTRF= connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='WT' and condition='TR' and sex='F'")
    WTTRF_values = [row[0] for row in WTTRF]
    # print WTTRF_values


    WTDDM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='WT' and condition='DD' and sex='M'")
    WTDDM_values = [row[0] for row in WTDDM]
    # print WTDDM_values
    WTDDF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='WT' and condition='DD' and sex='F'")
    WTDDF_values = [row[0] for row in WTDDF]
    # print WTDDF_values


    KOTRM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='KO' and condition='TR' and sex='M'")
    KOTRM_values = [row[0] for row in KOTRM]
    # print KOTRM_values
    KOTRF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='KO' and condition='TR' and sex='F'")
    KOTRF_values = [row[0] for row in KOTRF]
    # print KOTRF_values


    KODDM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='KO' and condition='DD' and sex='M'")
    KODDM_values = [row[0] for row in KODDM]
    # print KODDM_values
    KODDF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='KO' and condition='DD' and sex='F'")
    KODDF_values = [row[0] for row in KODDF]
    # print KODDF_values

    return WTTR_values,WTDD_values,KOTR_values,KODD_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values

# WTTR_values,WTDD_values,KOTR_values,KODD_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values = summary_graphs('P21','soma_size')

def dev_graphs(metric):
    import sqlite3
    connection = sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')

    WT_P7 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P7' and genotype='WT' and condition='TR'")
    WTTR_P7_values = [row[0] for row in  WT_P7]
    # print WTTR_P7_values

    WT_P12 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P12' and genotype='WT' and condition='TR'")
    WTTR_P12_values = [row[0] for row in  WT_P12]
    # print WTTR_P12_values

    WT_P16 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P16' and genotype='WT' and condition='TR'")
    WTTR_P16_values = [row[0] for row in  WT_P16]
    # print WTTR_P16_values

    WT_P21 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P21' and genotype='WT' and condition='TR'")
    WTTR_P21_values = [row[0] for row in  WT_P21]
    # print WTTR_P21_values

    WT_P30 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='WT' and condition='TR'")
    WTTR_P30_values = [row[0] for row in  WT_P30]
    # print WTTR_P30_values

    KO_P7 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P7' and genotype='KO' and condition='TR'")
    KOTR_P7_values = [row[0] for row in  KO_P7]
    # print  KOTR_P7_values

    KO_P12 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P12' and genotype='KO' and condition='TR'")
    KOTR_P12_values = [row[0] for row in KO_P12]
    # print  KOTR_P12_values

    KO_P16 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P16' and genotype='KO' and condition='TR'")
    KOTR_P16_values = [row[0] for row in KO_P16]
    # print  KOTR_P16_values

    KO_P21 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P21' and genotype='KO' and condition='TR'")
    KOTR_P21_values = [row[0] for row in KO_P21]
    # print  KOTR_P21_values

    KO_P30 = connection.execute(
        "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='TR'")
    KOTR_P30_values = [row[0] for row in  KO_P30]
    # print  KOTR_P30_values

    return WTTR_P7_values, WTTR_P12_values, WTTR_P16_values, WTTR_P21_values, WTTR_P30_values, KOTR_P7_values, KOTR_P12_values, KOTR_P16_values, KOTR_P21_values, KOTR_P30_values

def sholl_values(age, metric):

    import sqlite3
    connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
    # cursor = connection.execute("select genotype from Neurons")
    # for row in cursor:
    #     print row

    #By Genotype and Condition
    WTTR = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '"+age+"'and genotype='WT' and condition='TR'")
    WTTR_values = [row[0] for row in WTTR]
    # print WTTR_values
    WTTR_values = [strings.split(',') for strings in WTTR_values]
    # print WTTR_values
    WTTR_values = [[int(sholl_intersections) for sholl_intersections in values] for values in WTTR_values]
    # print WTTR_values

    WTDD = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='WT' and condition='DD'")
    WTDD_values = [row[0] for row in WTDD]
    # print WTDD_values
    WTDD_values = [strings.split(',') for strings in WTDD_values]
    # print WTDD_values
    WTDD_values = [[int(sholl_intersections) for sholl_intersections in values] for values in WTDD_values]
    # print WTDD_values

    KOTR = connection.execute("select "+metric+ " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '"+age+"'and genotype='KO' and condition='TR'")
    KOTR_values = [row[0] for row in KOTR]
    KOTR_values = [strings.split(',') for strings in KOTR_values]
    KOTR_values = [[int(sholl_intersections) for sholl_intersections in values] for values in KOTR_values]
    # print KOTR_values

    KODD = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = '" + age + "'and genotype='KO' and condition='DD'")
    KODD_values = [row[0] for row in KODD]
    KODD_values = [strings.split(',') for strings in KODD_values]
    KODD_values = [[int(sholl_intersections) for sholl_intersections in values] for values in KODD_values]
    # print KODD_values

    return WTTR_values, WTDD_values, KOTR_values, KODD_values

def recover_graphs(metric):

    import sqlite3
    connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
    # cursor = connection.execute("select genotype from Neurons")
    # for row in cursor:
    #     print row

    #By Genotype and Condition
    WTTR = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30'and genotype='WT' and condition='TR'")
    WTTR_values = [row[0] for row in WTTR]
    print WTTR_values

    WTDD = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30'and genotype='WT' and condition='DD'")
    WTDD_values = [row[0] for row in WTDD]
    print WTDD_values

    WTDL = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30'and genotype='WT' and condition='DL'")
    WTDL_values = [row[0] for row in WTDL]
    print WTDD_values

    KOTR = connection.execute("select "+metric+ " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='TR'")
    KOTR_values = [row[0] for row in KOTR]
    print KOTR_values

    KODD = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30'and genotype='KO' and condition='DD'")
    KODD_values = [row[0] for row in KODD]
    print KODD_values

    KODL = connection.execute( "select " + metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30'and genotype='KO' and condition='DL'")
    KODL_values = [row[0] for row in KODL]
    print KODD_values

    #By Genotype, Condition, and Sex
    WTTRM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30'and genotype='WT' and condition='TR' and sex='M'")
    WTTRM_values = [row[0] for row in WTTRM]
    # print WTTRM_values
    WTTRF= connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='WT' and condition='TR' and sex='F'")
    WTTRF_values = [row[0] for row in WTTRF]
    print WTTRF_values


    WTDDM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='WT' and condition='DD' and sex='M'")
    WTDDM_values = [row[0] for row in WTDDM]
    print WTDDM_values
    WTDDF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='WT' and condition='DD' and sex='F'")
    WTDDF_values = [row[0] for row in WTDDF]
    print WTDDF_values

    WTDLM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='WT' and condition='DL' and sex='M'")
    WTDLM_values = [row[0] for row in WTDLM]
    print WTDDM_values
    WTDLF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='WT' and condition='DL' and sex='F'")
    WTDLF_values = [row[0] for row in WTDLF]
    print WTDDF_values

    KOTRM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='TR' and sex='M'")
    KOTRM_values = [row[0] for row in KOTRM]
    # print KOTRM_values
    KOTRF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='TR' and sex='F'")
    KOTRF_values = [row[0] for row in KOTRF]
    print KOTRF_values

    KODDM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='DD' and sex='M'")
    KODDM_values = [row[0] for row in KODDM]
    print KODDM_values
    KODDF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='DD' and sex='F'")
    KODDF_values = [row[0] for row in KODDF]
    print KODDF_values

    KODLM = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='DL' and sex='M'")
    KODLM_values = [row[0] for row in KODLM]
    print KODDM_values
    KODLF = connection.execute("select "+metric + " from Neurons left join Animals on neurons.animal_id = animals.animal_id where age = 'P30' and genotype='KO' and condition='DL' and sex='F'")
    KODLF_values = [row[0] for row in KODLF]
    # print KODLF_values

    # print WTTR_values,WTDD_values,WTDL_values,KOTR_values,KODD_values, KODL_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,WTDLM_values, WTDLF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values, KODLM_values, KODLF_values

    return WTTR_values,WTDD_values,WTDL_values,KOTR_values,KODD_values, KODL_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,WTDLM_values, WTDLF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values, KODLM_values, KODLF_values

# WTTR_values,WTDD_values,KOTR_values,KODD_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values = summary_graphs('P21','soma_size')

