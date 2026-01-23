# 下载资源 / Downloads

本目录用于存放可下载的工具和资源文件。

This directory contains downloadable tools and resource files.

## 目录结构 / Directory Structure

```
downloads/
├── tools/          # Windows 工具和软件 / Windows tools and software
│   ├── modbuspoll/ # Modbus 测试工具 / Modbus testing tools
│   └── ...
└── README.md       # 本文件 / This file
```

## 使用说明 / Usage Instructions

### 中文说明

1. **添加工具文件**：将工具文件放在对应的子目录中，例如：
   - Windows 工具：`downloads/tools/modbuspoll/`
   
2. **在文档中引用**：在 Markdown 文档中使用相对路径或绝对路径链接到下载文件：
   ```markdown
   [下载 ModbusPoll 工具](../../../../../../downloads/tools/modbuspoll/modbuspoll-setup.exe)
   ```
   
   或使用绝对路径（推荐）：
   ```markdown
   [下载 ModbusPoll 工具](/downloads/tools/modbuspoll/modbuspoll-setup.exe)
   ```

3. **添加下载说明**：使用美观的格式展示下载链接：
   ```markdown
   ## 工具下载
   
   ### ModbusPoll 工具
   
   ModbusPoll 是一个 Modbus 主站仿真器，用于测试 Modbus 设备。
   
   - **版本**: 9.0.0
   - **文件大小**: 5.2 MB
   - **下载**: [:material-download: 下载 ModbusPoll](../../../../../../downloads/tools/modbuspoll/modbuspoll-setup.exe)
   ```

### English Instructions

1. **Add Tool Files**: Place tool files in the corresponding subdirectory, for example:
   - Windows tools: `downloads/tools/modbuspoll/`
   
2. **Reference in Documentation**: Use relative or absolute paths to link to download files in Markdown:
   ```markdown
   [Download ModbusPoll Tool](../../../../../../downloads/tools/modbuspoll/modbuspoll-setup.exe)
   ```
   
   Or use absolute paths (recommended):
   ```markdown
   [Download ModbusPoll Tool](/downloads/tools/modbuspoll/modbuspoll-setup.exe)
   ```

3. **Add Download Instructions**: Use beautiful formatting to display download links:
   ```markdown
   ## Tool Downloads
   
   ### ModbusPoll Tool
   
   ModbusPoll is a Modbus master simulator for testing Modbus devices.
   
   - **Version**: 9.0.0
   - **File Size**: 5.2 MB
   - **Download**: [:material-download: Download ModbusPoll](../../../../../../downloads/tools/modbuspoll/modbuspoll-setup.exe)
   ```

## 注意事项 / Notes

### 中文

- **大文件处理**：对于超过 100MB 的文件，建议使用 Git LFS 或外部存储服务
- **版本管理**：为每个工具创建版本号子目录，便于管理多个版本
- **文档同步**：更新工具时，记得同步更新文档中的版本号和说明

### English

- **Large Files**: For files over 100MB, consider using Git LFS or external storage
- **Version Management**: Create version subdirectories for each tool to manage multiple versions
- **Documentation Sync**: When updating tools, remember to update version numbers and descriptions in documentation
