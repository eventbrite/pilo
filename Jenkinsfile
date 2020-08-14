@Library('eb-jenkins-library') _

def repoName = 'pilo'

timestamps {
    switch (jobType.determineJobType()) {
        case jobType.PULL_REQUEST:
            testContainer {
                appName=repoName
            }
            break
        case jobType.INVOKE_RELEASE:
            invokeReleasePR {
                appName=repoName
                publishReleaseWheel=true
            }
            break
    }
}
