input_str = ''' implementation("com.github.hkirk:java-html2image:0.9")

    implementation("com.vdurmont:emoji-java:5.1.1")
    compile "com.github.jkcclemens:khttp:0.1.0"

    implementation 'io.github.shashankn:qr-terminal:1.0.0'

    implementation("org.jetbrains.exposed:exposed-core:0.36.1")
    implementation("org.jetbrains.exposed:exposed-dao:0.36.1")
    implementation("org.jetbrains.exposed:exposed-java-time:0.36.1")
    implementation("org.jetbrains.exposed:exposed-jdbc:0.36.1")


    implementation 'org.bitcoinj:bitcoinj-core:0.16.1'
    implementation 'com.github.nmac427:pultusorm:v1.7'
    implementation 'org.junit.jupiter:junit-jupiter:5.4.2'

    compile 'com.github.turasa:signal-service-java:2.15.3_unofficial_2'
    compile 'org.bouncycastle:bcprov-jdk15on:1.64'
    compile 'net.sourceforge.argparse4j:argparse4j:0.8.1'
    compile 'org.freedesktop.dbus:dbus-java:2.7.0'
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk8:$kotlin_version"'''

# print(input_str)

# replace 'compile' with 'implementation'
# wrap in quotes
# split on colons and replace with quotes and comma separator

clean_str1 = input_str.strip().replace('compile', 'implementation').replace('\'', '"')

tokens = clean_str1.split('implementation')
out_tokens = []

for token in tokens:
    if token.strip() != '':
        new_token = "implementation(" + token.strip().replace(":", '", "') + ")"
        new_token = new_token.replace("((", "(").replace("))", ")")
        print(new_token)
        out_tokens.append(new_token)

# print(out_tokens)

# print(tokens)
