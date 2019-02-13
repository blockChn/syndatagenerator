import logging
import pandas as pd
from tabulate import tabulate

from core import container
from core.random_generators import SequencialGenerator, FakerGenerator, NumpyRandomGenerator
import core.util_functions as util_functions


util_functions.setup_logging()

example_container = container.Container(name="example1",
                                        master_seed=1234)

id_gen = SequencialGenerator(prefix="PERSON_")

name_gen = FakerGenerator(method="name", seed=next(example_container.seeder))

age_gen = NumpyRandomGenerator(method="choice",   a=[20,30,40, 60],
                                              p=[0.2,0.3,0.2, 0.3],seed=next(example_container.seeder))

person = example_container.create_population(
    name="person", size=1000, ids_gen=id_gen)
person.create_attribute("name", init_gen=name_gen)
person.create_attribute("age", init_gen=age_gen)


logging.info("\n" +
             tabulate(person.to_dataframe().head(10),
                      headers='keys', tablefmt='psql')
             )
