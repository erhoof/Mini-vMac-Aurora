cmake_minimum_required(VERSION 3.5)

project(ru.erhoof.minivmac LANGUAGES C)

include(FindPkgConfig)
pkg_search_module(AURORA auroraapp REQUIRED)
pkg_search_module(AURORA auroraapp_i18n REQUIRED)
pkg_search_module(AURORA sdl2 REQUIRED)
pkg_search_module(AURORA glesv2 REQUIRED)

find_package(SDL2 REQUIRED)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(short_name minivmac)

set(CMAKE_SKIP_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/lib")

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DMACII")

set(BASE_SOURCES
        src/M68KCpuEmulator.c
        src/M68KInstructionTable.c
        src/GlobalGlue.c
        src/ViaEmulator.c
        src/Via2Emulator.c
        src/IwmEmulator.c
        src/SccEmulator.c
        src/RtcEmulator.c
        src/RomEmulator.c
        src/ScsiEmulator.c
        src/SonyEmulator.c
        src/ScreenEmulator.c
        src/MouseEmulator.c
        src/KeyboardEmulator.c
        src/AdbEmulator.c
        src/SoundEmulator.c
        src/AppleSoundEmulator.c
        src/VideoCardEmulator.c
        src/platforms/SDL2.c
)

set(SDL_SOURCES
        src/platforms/SDL_WithRom.c
)

set(MAIN_SOURCES
        src/ProgramMain.c
)

add_library (minivmac_base STATIC ${BASE_SOURCES})
target_link_libraries(minivmac_base SDL2::SDL2)

add_executable(${PROJECT_NAME} ${MAIN_SOURCES})

target_compile_definitions(${PROJECT_NAME} PRIVATE
    $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>
)
target_include_directories(${PROJECT_NAME} PRIVATE
    $<BUILD_INTERFACE:
    ${AURORA_INCLUDE_DIRS}
>)
target_link_libraries(${PROJECT_NAME} PRIVATE
    minivmac_base
    ${AURORA_LDFLAGS}
)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

set(IconSize 86x86 108x108 128x128 172x172)
foreach(_size IN LISTS IconSize)
    install(FILES icons/${_size}/${PROJECT_NAME}.png DESTINATION share/icons/hicolor/${_size}/apps)
endforeach()

install(FILES ${PROJECT_NAME}.desktop
    DESTINATION share/applications
)

# Get the other files reachable from the project tree in Qt Creator
file(GLOB_RECURSE IconFiles "icons" "*.png")
set(RESOURCE_FILES ${IconFiles})

add_custom_target(distfiles
    SOURCES
        ${PROJECT_NAME}.desktop
        rpm/${PROJECT_NAME}.spec
        rpm/${PROJECT_NAME}.changes.in
        rpm/${PROJECT_NAME}.changes.run.in
        ${TsFiles}
        ${IconFiles})

file(WRITE "${CMAKE_BINARY_DIR}/QtCreatorDeployment.txt"
    "${CMAKE_INSTALL_PREFIX}
    ${CMAKE_BINARY_DIR}/${PROJECT_NAME}:bin
")
