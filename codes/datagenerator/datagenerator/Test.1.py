import logging
import pandas  as pd
from tabulate import tabulate 

from core import container
from core.random_generators import SequencialGenerator, FakerGenerator, NumpyRandomGenerator
import core.util_functions as util_functions


util_functions.setup_logging()

example_container = container.Container(name="example1", 
                               master_seed=12345,
                               start=pd.Timestamp("1 Jan 2017 00:00"),
                               step_duration=pd.Timedelta("1h"))

id_gen = SequencialGenerator(prefix="PERSON_")

name_gen = FakerGenerator(method="name", seed=next(example_container.seeder))

person = example_container.create_population(name="person", size=1000, ids_gen=id_gen)
person.create_attribute("NAME", init_gen=name_gen)


logging.info("\n" + 
  tabulate(person.to_dataframe().head(10), headers='keys', tablefmt='psql')
)



