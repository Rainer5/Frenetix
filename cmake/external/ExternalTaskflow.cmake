include(FetchContent)
include(utils/FetchContentHelper)

set(taskflow_version 3.7.0)

FetchContent_Declare_Fallback(
    taskflow

    SYSTEM

    URL "https://github.com/taskflow/taskflow/archive/refs/tags/v${taskflow_version}.tar.gz"
    URL_HASH SHA256=788b88093fb3788329ebbf7c7ee05d1f8960d974985a301798df01e77e04233b

    #GIT_REPOSITORY "https://github.com/taskflow/taskflow.git"
    #GIT_TAG 12f8bd4e970ab27fd3dee3bffa24b5b48b54ba39
)

set(TF_BUILD_EXAMPLES OFF)
set(TF_BUILD_TESTS OFF)

FetchContent_MakeAvailable(taskflow)

set_property(DIRECTORY ${taskflow_SOURCE_DIR} PROPERTY EXCLUDE_FROM_ALL ON)

