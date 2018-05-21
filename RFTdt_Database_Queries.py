def summary_graphs(dpi, metric):

    import sqlite3
    connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
    # cursor = connection.execute("select * from RFTdt_Neurons")
    # for row in cursor:
    #     print row

    #By Genotype and Condition
    WTTR = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '"+dpi+"'and genotype='WT' and condition='TR'")
    WTTR_values = [row[0] for row in WTTR]
    # print WTTR_values
#
#     WTDD = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='WT' and condition='DD'")
#     WTDD_values = [row[0] for row in WTDD]
#     # print WTDD_values
#
    FLXTR = connection.execute("select "+metric+ " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '"+dpi+"'and genotype='FLX' and condition='TR'")
    FLXTR_values = [row[0] for row in FLXTR]
    # print FLXTR_values
#
#     FLXDD = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='FLX' and condition='DD'")
#     FLXDD_values = [row[0] for row in FLXDD]
#     # print FLXDD_values
#
#
#     #By Genotype, Condition, and Sex
#     WTTRM = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='WT' and condition='TR' and sex='M'")
#     WTTRM_values = [row[0] for row in WTTRM]
#     # print WTTRM_values
#     WTTRF= connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='WT' and condition='TR' and sex='F'")
#     WTTRF_values = [row[0] for row in WTTRF]
#     # print WTTRF_values
#
#
#     WTDDM = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='WT' and condition='DD' and sex='M'")
#     WTDDM_values = [row[0] for row in WTDDM]
#     # print WTDDM_values
#     WTDDF = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='WT' and condition='DD' and sex='F'")
#     WTDDF_values = [row[0] for row in WTDDF]
#     # print WTDDF_values
#
#
#     FLXTRM = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='FLX' and condition='TR' and sex='M'")
#     FLXTRM_values = [row[0] for row in FLXTRM]
#     # print FLXTRM_values
#     FLXTRF = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='FLX' and condition='TR' and sex='F'")
#     FLXTRF_values = [row[0] for row in FLXTRF]
#     # print FLXTRF_values
#
#
#     FLXDDM = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='FLX' and condition='DD' and sex='M'")
#     FLXDDM_values = [row[0] for row in FLXDDM]
#     # print FLXDDM_values
#     FLXDDF = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='FLX' and condition='DD' and sex='F'")
#     FLXDDF_values = [row[0] for row in FLXDDF]
#     # print FLXDDF_values
#
    return WTTR_values,FLXTR_values
#
# # WTTR_values,WTDD_values,FLXTR_values,FLXDD_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,FLXTRM_values,FLXTRF_values,FLXDDM_values,FLXDDF_values = summary_graphs('09dpi','soma_size')
#
def dev_graphs(metric):
    import sqlite3
    connection = sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
    cursor = connection.execute("select * from RFTdt_Neurons")
    # for row in cursor:
    #     print row

    WT_03dpi = connection.execute("select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '03dpi' and genotype='WT' and condition='TR'")
    WTTR_dpi03_values = [row[0] for row in  WT_03dpi]
    # print WTTR_03dpi_values

    WT_05dpi = connection.execute("select "+ metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '05dpi' and genotype='WT' and condition='TR'")
    WTTR_dpi05_values = [row[0] for row in  WT_05dpi]
    # print WTTR_05dpi_values

    WT_07dpi = connection.execute("select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '07dpi' and genotype='WT' and condition='TR'")
    WTTR_dpi07_values = [row[0] for row in  WT_07dpi]
    # print WTTR_07dpi_values

    WT_09dpi = connection.execute("select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '09dpi' and genotype='WT' and condition='TR'")
    WTTR_dpi09_values = [row[0] for row in  WT_09dpi]
    # print WTTR_09dpi_values

    WT_12dpi = connection.execute("select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '12dpi' and genotype='WT' and condition='TR'")
    WTTR_dpi12_values = [row[0] for row in  WT_12dpi]
    # print WTTR_12dpi_values

    FLX_03dpi = connection.execute( "select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '03dpi' and genotype='FLX' and condition='TR'")
    FLXTR_dpi03_values = [row[0] for row in  FLX_03dpi]
    # print  FLXTR_03dpi_values

    FLX_05dpi = connection.execute("select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '05dpi' and genotype='FLX' and condition='TR'")
    FLXTR_dpi05_values = [row[0] for row in FLX_05dpi]
    # print  FLXTR_05dpi_values

    FLX_07dpi = connection.execute( "select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '07dpi' and genotype='FLX' and condition='TR'")
    FLXTR_dpi07_values = [row[0] for row in FLX_07dpi]
    # print  FLXTR_07dpi_values

    FLX_09dpi = connection.execute( "select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '09dpi' and genotype='FLX' and condition='TR'")
    FLXTR_dpi09_values = [row[0] for row in FLX_09dpi]
    # print  FLXTR_09dpi_values

    FLX_12dpi = connection.execute("select " + metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '12dpi' and genotype='FLX' and condition='TR'")
    FLXTR_dpi12_values = [row[0] for row in  FLX_12dpi]
    # print  FLXTR_12dpi_values

    return WTTR_dpi03_values,WTTR_dpi05_values, WTTR_dpi07_values, WTTR_dpi09_values, WTTR_dpi12_values, FLXTR_dpi03_values,FLXTR_dpi05_values, FLXTR_dpi07_values, FLXTR_dpi09_values, FLXTR_dpi12_values

def sholl_values(dpi, metric):

    import sqlite3
    connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\RFTdt_Dendrite_Analysis.db')
    # cursor = connection.execute("select genotype from RFTdt_Neurons")
    # for row in cursor:
    #     print row

    #By Genotype and Condition
    WTTR = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '"+dpi+"'and genotype='WT' and condition='TR'")
    WTTR_values = [row[0] for row in WTTR]
    # print WTTR_values
    WTTR_values = [strings.split(',') for strings in WTTR_values]
    # print WTTR_values
    WTTR_values = [[int(sholl_intersections) for sholl_intersections in values] for values in WTTR_values]
    # print WTTR_values

    # WTDD = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='WT' and condition='DD'")
    # WTDD_values = [row[0] for row in WTDD]
    # # print WTDD_values
    # WTDD_values = [strings.split(',') for strings in WTDD_values]
    # # print WTDD_values
    # WTDD_values = [[int(sholl_intersections) for sholl_intersections in values] for values in WTDD_values]
    # # print WTDD_values

    FLXTR = connection.execute("select "+metric+ " from RFTdt_Neurons left join RFTdt_Animals on rftdt_neurons.animal_id = rftdt_animals.animal_id where dpi = '"+dpi+"'and genotype='FLX' and condition='TR'")
    FLXTR_values = [row[0] for row in FLXTR]
    FLXTR_values = [strings.split(',') for strings in FLXTR_values]
    FLXTR_values = [[int(sholl_intersections) for sholl_intersections in values] for values in FLXTR_values]
    # print FLXTR_values

    # FLXDD = connection.execute("select "+metric + " from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where dpi = '" + dpi + "'and genotype='FLX' and condition='DD'")
    # FLXDD_values = [row[0] for row in FLXDD]
    # FLXDD_values = [strings.split(',') for strings in FLXDD_values]
    # FLXDD_values = [[int(sholl_intersections) for sholl_intersections in values] for values in FLXDD_values]
    # # print FLXDD_values

    return WTTR_values, FLXTR_values


