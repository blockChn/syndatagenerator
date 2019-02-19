import logging
import pandas as pd
from tabulate import tabulate

from core import container, operations
from core.random_generators import SequencialGenerator, FakerGenerator, NumpyRandomGenerator, ConstantDependentGenerator, ConstantGenerator
import core.util_functions as util_functions


util_functions.setup_logging()

example_container = container.Container(name="example1",
                                        master_seed=1234, start=pd.Timestamp("1 Jan 2017 00:00"),
                                        step_duration=pd.Timedelta("1h"))

id_gen = SequencialGenerator(prefix="PERSON_")

name_gen = FakerGenerator(method="name", seed=next(example_container.seeder))

age_gen = NumpyRandomGenerator(method="choice",   a=[20, 30, 40, 60],
                               p=[0.2, 0.3, 0.2, 0.3], seed=next(example_container.seeder))

gender_gen = NumpyRandomGenerator(method="choice",   a=["male", "female"],
                                  p=[0.6, 0.4], seed=next(example_container.seeder))

job_type_gen = NumpyRandomGenerator(method="choice",   a=["salaried", "non_salaried", "job_type3", "job_type4", "job_type5"],
                                  p=[0.2, 0.2,0.2,0.2,0.2], seed=next(example_container.seeder))

person = example_container.create_population(
    name="person", size=1000, ids_gen=id_gen)
person.create_attribute("name", init_gen=name_gen)
person.create_attribute("gender", init_gen=gender_gen)
person.create_attribute("age", init_gen=age_gen)
person.create_attribute("job_type", init_gen=job_type_gen)

#########
logging.info("\n" + tabulate(person.to_dataframe().head(10),
                             headers='keys', tablefmt='psql')
             )

persona_population = example_container.create_story(
    name="persona_population",
    initiating_population=example_container.populations["person"],
    member_id_field="PERSON_ID",
    timer_gen=ConstantDependentGenerator(value=1)
)

logging.info(" PERSONA STORY CREATED")

persona_population.set_operations(
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"gender": "GENDER"}),
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"age": "AGE"}),
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"job_type": "JOB TYPE"}),
    operations.FieldLogger(log_id="persona")
)

logging.info(" PERSONA Operation")

example_container.run(
    duration=pd.Timedelta("2h"),
    log_output_folder="output/example_scenario",
    delete_existing_logs=True
)

#########

#########
logging.info("\n" + tabulate(person.to_dataframe().head(10),
                             headers='keys', tablefmt='psql')
             )

person_population = example_container.create_story(
    name="person_population",
    initiating_population=example_container.populations["person"],
    member_id_field="PERSON_ID",
    timer_gen=ConstantDependentGenerator(value=1)
)

logging.info(" PERSONA STORY CREATED")

person_population.set_operations(
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"name": "NAME"}),
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"gender": "GENDER"}),
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"age": "AGE"}),
    example_container.populations["person"].ops.lookup(
        id_field="PERSON_ID", select={"job_type": "JOB TYPE"}),
    operations.FieldLogger(log_id="person")
)

logging.info(" PERSONA Operation")

example_container.run(
    duration=pd.Timedelta("2h"),
    log_output_folder="output/example_scenario",
    delete_existing_logs=True
)

#########
