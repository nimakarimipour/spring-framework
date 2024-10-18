import os

nullaway_config = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<serialization>
	<suggest active="true" enclosing="true"/>
	<fieldInitInfo active="true"/>
	<path>/home/nima/Developer/nullness-benchmarks/spring-framework/{}/annotator-out/0</path>
	<uuid>3db91ec7-19a7-4a55-bbdf-22b3722ff912</uuid>
</serialization>
"""

scanner_config = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<scanner>
	<serialization active="true"/>
	<uuid>eaa892b1-9c85-4193-ae16-30fef023db49</uuid>
	<path>//home/nima/Developer/nullness-benchmarks/spring-framework/{}/annotator-out/0</path>
	<processor>
		<LOMBOK active="true"/>
	</processor>
	<annotations/>
</scanner>
"""

current_dir = os.getcwd()
for module in os.listdir(current_dir):
    if module.startswith("spring"):
        # make annotator-out directory
        os.system("rm -rvf {}/{}/annotator-out".format(current_dir, module))
        os.system("mkdir -p {}/{}/annotator-out/".format(current_dir, module))
        os.system("mkdir -p {}/{}/annotator-out/0".format(current_dir, module))

        # write nullaway config to nullaway.xml
        with open("{}/{}/annotator-out/nullaway.xml".format(current_dir, module), "w") as f:
            f.write(nullaway_config.format(module))

		# write scanner config to scanner.xml
        with open("{}/{}/annotator-out/scanner.xml".format(current_dir, module), "w") as f:
            f.write(scanner_config.format(module))





